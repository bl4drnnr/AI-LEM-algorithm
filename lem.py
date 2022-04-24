from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getParsedPairs
DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
ALL_CLASSES = ALL_POSSIBLE_ATTRIBUTES[KEY_ATTRIBUTE]

INPUT_DATA_LENGTH = len(DATA)
GENERATED_RULES = []
PARSED_PAIRS = getParsedPairs()

Bs = {}

parsedRecordsAndPairs = {}

for x in range(INPUT_DATA_LENGTH):
    for pair in PARSED_PAIRS:
        if DATA[x][list(pair)[0]] == pair[list(pair)[0]]:
            parsedName = str(list(pair)[0]) + '_' + str(pair[list(pair)[0]])
            if parsedRecordsAndPairs.get(parsedName) is None:
                parsedRecordsAndPairs[parsedName] = [{x + 1: DATA[x]}]
            else:
                parsedRecordsAndPairs[parsedName].append({x + 1: DATA[x]})

for x in range(INPUT_DATA_LENGTH):
    for attr, value in ALL_CLASSES.items():
        if DATA[x][KEY_ATTRIBUTE] == value:
            if Bs.get(attr) is None:
                Bs[attr] = [{x + 1: DATA[x]}]
            else:
                Bs[attr].append({x + 1: DATA[x]})

for attr, value in Bs.items():
    print(attr, value)
