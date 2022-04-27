from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getParsedPairs, parseName
from common import getPL, extractIndexes, generateRule, extractPL, printRules, pairInB, indexesInB, uniteRecords
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


def lem(extractedIdx, tg, currentRule):
    extractedIndexesB = extractedIdx
    unitedRecordsForNewPair = []

    # Extracting P and L
    recordsPl = extractPL(tg, extractedIndexesB)

    maxPandMinLRecord = getPL(recordsPl)
    maxPandMinLIndexes = extractIndexes(maxPandMinLRecord['records'])

    pairInBres = pairInB(maxPandMinLIndexes, extractedIndexesB)

    # If pair in B - generate rule
    if pairInBres:
        # Write down rule, rewrite G (extractedIndexesB), rewrite TG and iterate one more time
        GENERATED_RULES.append({
            'rule': generateRule([maxPandMinLRecord], currentRule),
            'records': maxPandMinLIndexes
        })

        updatedExtractedIndexesB = []
        for ruleIndex in extractedIndexesB:
            if ruleIndex not in maxPandMinLIndexes:
                updatedExtractedIndexesB.append(ruleIndex)
        extractedIndexesB = updatedExtractedIndexesB

        # Update TG below
        updatedTG = {}
        for t in tg:
            if t != maxPandMinLRecord['recType']:
                updatedTG[t] = tg[t]

        lem(extractedIndexesB, updatedTG, currentRule)
    else:
        # Find record to unite
        uniteRecords()
        unitedRecordsArray = [maxPandMinLRecord]

        # Unite records and check, if their indexes are in B
        unitedRecordsForNewPair.append(maxPandMinLIndexes)
        tempRecordsPL = []
        for rec in recordsPl:
            if rec != maxPandMinLRecord:
                tempRecordsPL.append(rec)
        unitedRecordsArray.append(getPL(tempRecordsPL))
        unitedRecordsForNewPair.append(extractIndexes(getPL(tempRecordsPL)['records']))

        # United records common part
        unitedRecordsCommonPart = []
        for a in unitedRecordsForNewPair[0]:
            for b in unitedRecordsForNewPair[1:]:
                for ixd in b:
                    if ixd == a:
                        unitedRecordsCommonPart.append(a)

        # Check if new common indexes are in B, and if it is, generate new rule
        newCommonIndexesInB = indexesInB(extractedIndexesB, unitedRecordsCommonPart)
        GENERATED_RULES.append({
            'rule': generateRule(unitedRecordsArray, currentRule),
            'records': unitedRecordsCommonPart
        })


for attr, value in Bs.items():
    ruleResult = attr
    currentBs = value
    lem(extractIndexes(currentBs), TG, ruleResult)


printRules(GENERATED_RULES)
