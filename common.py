def lookForRuleAndRecordMatches(record, rule):
    t = []
    for x in record:
        for y in rule:
            if list(x)[0] == list(y)[0]:
                t.append(list(x)[0])

    return [len(t), len(record)]
