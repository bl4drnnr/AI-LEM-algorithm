from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getParsedPairs, parseName
from common import getPL, extractIndexes, generateRule, extractPL, printRules
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


def lem(extractedIdx, tg):
    extractedIndexesB = extractedIdx

    print("extractedIndexes: " + str(extractedIndexesB))

    # Extracting P and L
    recordsPl = extractPL(tg, extractedIndexesB)

    maxPandMinLRecord = getPL(recordsPl)
    maxPandMinLIndexes = extractIndexes(maxPandMinLRecord['records'])

    pairInB = True

    for idx in maxPandMinLIndexes:
        if idx not in extractedIndexesB:
            pairInB = False

    # If pair in B - generate rule
    if pairInB:
        # Write down rule, rewrite G (extractedIndexesB), and iterate one more time
        print("Rule " + str(generateRule(maxPandMinLRecord, 'srednie')) + " has been generated!")
        GENERATED_RULES.append(generateRule(maxPandMinLRecord, 'srednie'))

        updatedExtractedIndexesB = []
        for x in extractedIndexesB:
            if x not in maxPandMinLIndexes:
                updatedExtractedIndexesB.append(x)
        extractedIndexesB = updatedExtractedIndexesB

        # lem(extractedIndexesB, tg)
    else:
        # Find record to unite
        print("maxPandMinLRecord: " + str(maxPandMinLRecord))
        print("maxPandMinLIndexes: " + str(maxPandMinLIndexes))

    print('extractedIndexesB: ' + str(extractedIndexesB))
    print('------------')


for attr, value in Bs.items():
    ruleResult = attr
    currentBs = value
    lem(extractIndexes(currentBs), TG)


printRules(GENERATED_RULES)
