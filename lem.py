from parser import parseInputData, getAllPossibleAttributes, getKeyAttribute, getDecisionAttributes, getParsedPairs
DATA = parseInputData()
KEY_ATTRIBUTE = getKeyAttribute()
ALL_POSSIBLE_ATTRIBUTES = getAllPossibleAttributes()
INPUT_DATA_LENGTH = len(DATA)
GENERATED_RULES = []
PARSED_PAIRS = getParsedPairs()

parsedRecordsAndRules = []

for x in range(INPUT_DATA_LENGTH):
    for pair in PARSED_PAIRS:
        print()
