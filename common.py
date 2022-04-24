def lookForRuleAndRecordMatches(record, rule):
    t = []
    for x in record:
        for y in rule:
            if list(x)[0] == list(y)[0]:
                t.append(list(x)[0])

    return [len(t), len(record)]


def getPL(PL):
    mostRelatedPair = None
    pl = []
    P = []
    L = []
    for item in PL:
        pl.append(item['pl'])

    for item in pl:
        P.append(item[0])

    P = max(P)
    temp = []
    for item in pl:
        if item[0] == P:
            temp.append(item)

    for item in temp:
        L.append(item[1])

    L = min(L)

    for item in pl:
        if item[0] == P and item[1] == L:
            mostRelatedPair = item
    for item in PL:
        if item['pl'] == mostRelatedPair:
            mostRelatedPair = item
    return mostRelatedPair
    # mostRelatedPairs = []
    # P = max(P)
    # for item in PL:
    #     if item['pl'][0] == P:
    #         L.append(item['pl'][1])
    # L = min(L)
    # for item in PL:
    #     if item['pl'][0] == P and item['pl'][1] == L:
    #         mostRelatedPairs.append(item)
    # return mostRelatedPairs
