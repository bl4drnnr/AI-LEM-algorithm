from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getParsedPairs
from common import lookForRuleAndRecordMatches
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
            parsedName = str(list(pair)[0]) + '_' + str(pair[list(pair)[0]])
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
    oneRule = value
    mostRelatedPairs = []
    G = Bs
    P = []
    L = []
    PL = []
    for k, v in TG.items():
        oneKeyPair = v
        res = lookForRuleAndRecordMatches(oneKeyPair, oneRule)
        PL.append({'pl': res, 'records': oneKeyPair})
        P.append(res[0])

    P = max(P)
    for item in PL:
        if item['pl'][0] == P:
            L.append(item['pl'][1])
    L = min(L)
    for item in PL:
        if item['pl'][0] == P and item['pl'][1] == L:
            mostRelatedPairs.append(item)

    print(mostRelatedPairs[0]['records'])
    iterator = 0
    for item in mostRelatedPairs[0]['records']:
        for i in G[attr]:
            for a, v in i.items():
                if a == list(item)[0]:
                    iterator += 1
    if iterator == len(mostRelatedPairs[0]['records']):
        print(mostRelatedPairs[0]['records'])
    print()
