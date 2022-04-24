import json

f = open('input.json')
DATA = json.load(f)
DATA = DATA['inputdata']
ALL_POSSIBLE_ATTRIBUTES = {}


def getAllPossibleAttributes():
    return ALL_POSSIBLE_ATTRIBUTES


def getKeyAttribute():
    return list(DATA[0])[-1]


def getParsedPairs():
    possibleAttributes = getAllPossibleAttributes()
    parsedAttributes = []
    for attr, value in possibleAttributes.items():
        if attr != getKeyAttribute():
            for item in list(value):
                parsedAttributes.append({attr: possibleAttributes[attr][item]})
    return parsedAttributes


def parseName(name):
    return str(list(name)[0]) + '_' + str(name[list(name)[0]])


def deparseName(name):
    possibleAttributes = getAllPossibleAttributes()
    deparsedName = []
    for attr, value in possibleAttributes.items():
        if attr == name.split('_')[0]:
            deparsedName.append(attr)
            for a, v in value.items():
                if v == int(name.split('_')[1]):
                    deparsedName.append(a)
    return deparsedName


def parseInputData():
    # Get all possible attributes and classes
    for record in DATA:
        for attr, value in record.items():
            if ALL_POSSIBLE_ATTRIBUTES.get(attr) is None:
                ALL_POSSIBLE_ATTRIBUTES[attr] = {value: 0}
            else:
                if ALL_POSSIBLE_ATTRIBUTES[attr].get(value) is None:
                    ALL_POSSIBLE_ATTRIBUTES[attr][value] = 0
    # Parse those attributes and classes and give values
    for param in ALL_POSSIBLE_ATTRIBUTES:
        i = 0
        for attr, value in ALL_POSSIBLE_ATTRIBUTES[param].items():
            ALL_POSSIBLE_ATTRIBUTES[param][attr] += i
            i += 1
    # Parse input data
    for record in DATA:
        for attr, value in record.items():
            record[attr] = ALL_POSSIBLE_ATTRIBUTES[attr][value]
    return DATA
