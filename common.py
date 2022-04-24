def lookForRuleAndRecordMatches(record, rule):
    t = []
    for x in record:
        for y in rule:
            if list(x)[0] == list(y)[0]:
                t.append(list(x)[0])

    return [len(t), len(record)]


def getPL(P, L, PL):
    mostRelatedPairs = []
    P = max(P)
    for item in PL:
        if item['pl'][0] == P:
            L.append(item['pl'][1])
    L = min(L)
    for item in PL:
        if item['pl'][0] == P and item['pl'][1] == L:
            mostRelatedPairs.append(item)
    return mostRelatedPairs
