from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getDecisionAttributes, getParsedPairs
DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
INPUT_DATA_LENGTH = len(DATA)
GENERATED_RULES = []
PARSED_PAIRS = getParsedPairs()

parsedRecordsAndPairs = {}

for x in range(INPUT_DATA_LENGTH):
    for pair in PARSED_PAIRS:
        if DATA[x][list(pair)[0]] == pair[list(pair)[0]]:
            parsedName = str(list(pair)[0]) + str(pair[list(pair)[0]])
            if parsedRecordsAndPairs.get(parsedName) is None:
                parsedRecordsAndPairs[parsedName] = [DATA[x]]
            else:
                parsedRecordsAndPairs[parsedName].append(DATA[x])

for attr, value in parsedRecordsAndPairs.items():
    print(attr, value)
