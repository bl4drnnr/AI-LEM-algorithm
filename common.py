from parser import getKeyAttribute, deparseName
KEY_ATTRIBUTE = getKeyAttribute()


def lookForRuleAndRecordMatches(record, rule):
    t = []
    for x in record:
        for y in rule:
            if list(x)[0] == list(y)[0]:
                t.append(list(x)[0])

    return [len(t), len(record)]


def getPL(records):
    Ps = []
    Ls = []

    # Look for max P and min L
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


# def getPL(PL):
#     mostRelatedPair = None
#     pl = []
#     P = []
#     L = []
#     for item in PL:
#         pl.append(item['pl'])
#
#     for item in pl:
#         P.append(item[0])
#
#     P = max(P)
#     temp = []
#     for item in pl:
#         if item[0] == P:
#             temp.append(item)
#
#     for item in temp:
#         L.append(item[1])
#
#     L = min(L)
#
#     for item in pl:
#         if item[0] == P and item[1] == L:
#             mostRelatedPair = item
#     for item in PL:
#         if item['pl'] == mostRelatedPair:
#             mostRelatedPair = item
#     return mostRelatedPair


def extractIndexes(arr):
    indexes = []
    for item in arr:
        for attr, value in item.items():
            indexes.append(attr)
    return indexes


def generateRule(result, records):
    rule = "IF "
    deparsedName = deparseName(records['type'])
    rule += str(deparsedName[0]) + " = " + str(deparsedName[1])
    rule += " THEN " + str(KEY_ATTRIBUTE) + " = " + str(result)
    return rule
