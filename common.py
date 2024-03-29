from parser import getKeyAttribute, deparseName
KEY_ATTRIBUTE = getKeyAttribute()


# Look for max P and min L
def getPL(records):
    Ps = []
    Ls = []

    for item in records:
        Ps.append(item['PL'][0])
        Ls.append(item['PL'][1])

    PsAndLs = []

    for x in range(len(Ps)):
        PsAndLs.append([Ps[x], Ls[x]])

    maxP = max(Ps)
    tempPsAndLs = []
    tempLs = []

    for item in PsAndLs:
        if item[0] == maxP:
            tempPsAndLs.append(item)

    for item in tempPsAndLs:
        tempLs.append(item[1])

    minL = min(tempLs)
    maxPandMinL = None

    for item in PsAndLs:
        if item[0] == maxP and item[1] == minL:
            maxPandMinL = item

    for record in records:
        if record['PL'] == maxPandMinL:
            maxPandMinL = record

    return maxPandMinL


def extractPL(TG, extractedIndexesB):
    recordsPl = []
    for recordType, records in TG.items():
        P = 0
        L = len(records)
        for item in records:
            for index, record in item.items():
                if index in extractedIndexesB:
                    P += 1
        recordsPl.append({
            'recType': recordType,
            'records': records,
            'PL': [P, L]
        })
    return recordsPl


def extractIndexes(arr):
    indexes = []
    for item in arr:
        for attr, value in item.items():
            indexes.append(attr)
    return indexes


def generateRule(records, result):
    rule = "IF "

    if len(records) > 1:
        for i, rec in enumerate(records):
            deparsedName = deparseName(rec['recType'])
            if i != len(records) - 1:
                rule += str(deparsedName[0]) + " = " + str(deparsedName[1]) + " AND "
            else:
                rule += str(deparsedName[0]) + " = " + str(deparsedName[1])
    else:
        deparsedName = deparseName(records[0]['recType'])
        rule += str(deparsedName[0]) + " = " + str(deparsedName[1])

    rule += " THEN " + str(KEY_ATTRIBUTE) + " = " + str(result)

    return rule


def pairInB(maxPandMinLIndexes, extractedIndexesB):
    inB = True

    for idx in maxPandMinLIndexes:
        if idx not in extractedIndexesB:
            inB = False
    return inB


def uniteRecords(GENERATED_RULES, currentRule, extractedIndexesB, maxPandMinLRecord, maxPandMinLIndexes, unitedRecordsForNewPair, recordsPl):
    unitedRecordsArray = [maxPandMinLRecord]

    # Unite records and check, if their indexes are in B
    unitedRecordsForNewPair.append(maxPandMinLIndexes)

    unitedRecordsCommonPart = uniteRecordsUpdating(recordsPl, unitedRecordsArray, unitedRecordsForNewPair, GENERATED_RULES, currentRule)

    updatedTg = []
    for x in extractedIndexesB:
        if x not in unitedRecordsCommonPart:
            updatedTg.append(x)

    if len(updatedTg) > 0:
        updTg = []
        for rec in recordsPl:
            if extractIndexes(rec['records']) not in unitedRecordsForNewPair:
                updTg.append(rec)
        for i in updTg:
            i['PL'] = [0, 0]
            for updTgInx in updatedTg:
                if updTgInx in extractIndexes(i['records']):
                    i['PL'][0] += 1
            i['PL'][1] = len(extractIndexes(i['records']))
        unitedRecordsIndexes = []

        for x in updTg:
            t = True
            for y in updatedTg:
                if y not in extractIndexes(x['records']):
                    t = False
            if t:
                unitedRecordsIndexes.append(extractIndexes(x['records']))

        uni = []
        for uri in unitedRecordsIndexes:
            for utg in updTg:
                if extractIndexes(utg['records']) == uri:
                    uni.append(utg)

        GENERATED_RULES.append({
            'rule': generateRule(uni, currentRule),
            'records': updatedTg
        })


def uniteRecordsUpdating(recordsPl, unitedRecordsArray, unitedRecordsForNewPair, GENERATED_RULES, currentRule):
    updTg = []
    for rec in recordsPl:
        if rec not in unitedRecordsArray:
            updTg.append(rec)

    unitedRecordsArray.append(getPL(updTg))
    unitedRecordsForNewPair.append(extractIndexes(getPL(updTg)['records']))
    unitedRecordsCommonPart = []

    for a in unitedRecordsForNewPair[0]:
        for b in unitedRecordsForNewPair[1:]:
            for ixd in b:
                if ixd == a:
                    unitedRecordsCommonPart.append(a)

    GENERATED_RULES.append({
        'rule': generateRule(unitedRecordsArray, currentRule),
        'records': unitedRecordsCommonPart
    })
    return unitedRecordsCommonPart


def printRules(rules):
    for i, rule in enumerate(rules):
        print(f"{i + 1} - {rule['rule']} - {rule['records']}")

