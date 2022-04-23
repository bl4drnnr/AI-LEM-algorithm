from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getDecisionAttributes, getParsedPairs
DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
ALL_CLASSES = ALL_POSSIBLE_ATTRIBUTES[KEY_ATTRIBUTE]
INPUT_DATA_LENGTH = len(DATA)
GENERATED_RULES = []
PARSED_PAIRS = getParsedPairs()

parsedRecordsAndPairs = {}

for x in range(INPUT_DATA_LENGTH):
    for pair in PARSED_PAIRS:
        if DATA[x][list(pair)[0]] == pair[list(pair)[0]]:
            parsedName = str(list(pair)[0]) + '_' + str(pair[list(pair)[0]])
            if parsedRecordsAndPairs.get(parsedName) is None:
                parsedRecordsAndPairs[parsedName] = [DATA[x]]
            else:
                parsedRecordsAndPairs[parsedName].append(DATA[x])

B = []
for x in range(INPUT_DATA_LENGTH):
    if DATA[x][KEY_ATTRIBUTE] == ALL_CLASSES['srednie']:
        B.append(DATA[x])

for item in B:
    print(item)

G = B
T = []
PAIRED_RECORDS_AND_RULES = []

print('---------')

for attr, value in parsedRecordsAndPairs.items():
    print(attr, value)
    for x in value:
        for y in G:
            if x == y:
                PAIRED_RECORDS_AND_RULES.append(x)
    print(PAIRED_RECORDS_AND_RULES)
    PAIRED_RECORDS_AND_RULES = []
    print('-----------')
    # for item in G:
    #     print(attr, value)
