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
        for rec in records:
            deparsedName = deparseName(rec['recType'])
            rule += " " + str(deparsedName[0]) + " = " + str(deparsedName[1])
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


def indexesInB(B, indexes):
    newIndexesInB = True
    for x in indexes:
        if x not in B:
            newIndexesInB = False
    return newIndexesInB


def uniteRecords():
    return


def printRules(rules):
    for rule in rules:
        print(rule)
