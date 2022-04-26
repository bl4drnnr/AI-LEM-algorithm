from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getParsedPairs, parseName
from common import lookForRuleAndRecordMatches, getPL, extractIndexes, generateRule
DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
ALL_CLASSES = ALL_POSSIBLE_ATTRIBUTES[KEY_ATTRIBUTE]

INPUT_DATA_LENGTH = len(DATA)
GENERATED_RULES = []
PARSED_PAIRS = getParsedPairs()

Bs = {}

TG = {}

for x in range(INPUT_DATA_LENGTH):
    for pair in PARSED_PAIRS:
        if DATA[x][list(pair)[0]] == pair[list(pair)[0]]:
            parsedName = parseName(pair)
            if TG.get(parsedName) is None:
                TG[parsedName] = [{x + 1: DATA[x]}]
            else:
                TG[parsedName].append({x + 1: DATA[x]})


for x in range(INPUT_DATA_LENGTH):
    for attr, value in ALL_CLASSES.items():
        if DATA[x][KEY_ATTRIBUTE] == value:
            if Bs.get(attr) is None:
                Bs[attr] = [{x + 1: DATA[x]}]
            else:
                Bs[attr].append({x + 1: DATA[x]})

for attr, value in Bs.items():
    ruleResult = attr
    currentBs = value
    extractedIndexes = extractIndexes(currentBs)

    print("extractedIndexes: " + str(extractedIndexes))

    recordsPl = []
    # Extracting P and L
    for recordType, records in TG.items():
        P = 0
        L = len(records)
        for item in records:
            for index, record in item.items():
                if index in extractedIndexes:
                    P += 1
        recordsPl.append({
            'recType': recordType,
            'records': records,
            'PL': [P, L]
        })

    maxPandMinLRecord = getPL(recordsPl)
    maxPandMinLIndexes = extractIndexes(maxPandMinLRecord['records'])

    pairInB = True

    for idx in maxPandMinLIndexes:
        if idx not in extractedIndexes:
            pairInB = False

    # If pair in B - generate rule
    if pairInB:
        GENERATED_RULES.append(generateRule(maxPandMinLRecord, 'srednie'))

print(GENERATED_RULES)

# ----------------------------------------------------
# tempBs = Bs['srednie']
# GBSextractedIndexes = extractIndexes(tempBs)
# print("GBSextractedIndexes: " + str(GBSextractedIndexes))

# recordsPl = []

# Extracting P and L
# for recordType, records in TG.items():
#     P = 0
#     L = len(records)
#     for item in records:
#         for index, record in item.items():
#             if index in GBSextractedIndexes:
#                 P += 1
#     recordsPl.append({
#         'recType': recordType,
#         'records': records,
#         'PL': [P, L]
#     })

# maxPandMinLRecord = getPL(recordsPl)
# maxPandMinLIndexes = extractIndexes(maxPandMinLRecord['records'])

# pairInB = True
#
# for idx in maxPandMinLIndexes:
#     if idx not in GBSextractedIndexes:
#         pairInB = False
#
# # If pair in B - generate rule
# if pairInB:
#     GENERATED_RULES.append(generateRule(maxPandMinLRecord, 'srednie'))
# ----------------------------------------------------
# for attr, value in Bs.items():
#     oneRule = value
#     G = Bs
#     PL = []
#     for k, v in TG.items():
#         oneKeyPair = v
#         res = lookForRuleAndRecordMatches(oneKeyPair, oneRule)
#         PL.append({'pl': res, 'records': oneKeyPair, 'type': k})
#
#     mostRelatedPairs = getPL(PL)
#     extractedIndexesG = extractIndexes(G[attr])
#     extractedIndexesMostRelatedPairs = extractIndexes(mostRelatedPairs['records'])
#
#     if set(extractedIndexesMostRelatedPairs).issubset(set(extractedIndexesG)):
#         GENERATED_RULES.append(generateRule(attr, mostRelatedPairs))
#     else:
#         print("mostRelatedPairs: " + str(mostRelatedPairs))
#         print("extractedIndexesG: " + str(extractedIndexesG))
#         print("extractedIndexesMostRelatedPairs: " + str(extractedIndexesMostRelatedPairs))
#         print("---------")
#
# for rule in GENERATED_RULES:
#     print(rule)
