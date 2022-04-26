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

tempBs = Bs['srednie']
GBS = tempBs
GBSextractedIndexes = extractIndexes(tempBs)
print("GBSextractedIndexes: " + str(GBSextractedIndexes))

recordsPl = []

# Extracting P and L
for recordType, records in TG.items():
    P = 0
    L = len(records)
    for item in records:
        for index, record in item.items():
            if index in GBSextractedIndexes:
                P += 1
    recordsPl.append({
        'recType': recordType,
        'records': records,
        'PL': [P, L]
    })

Ps = []
Ls = []

# Look for max P and min L
for item in recordsPl:
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

for record in recordsPl:
    if record['PL'] == maxPandMinL:
        print(record)

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
