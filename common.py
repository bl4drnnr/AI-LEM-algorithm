def lookForRuleAndRecordMatches(record, rule):
    t = []
    r = []
    for x in record:
        for y in rule:
            if list(x)[0] == list(y)[0]:
                t.append(list(x)[0])
                r = len(record)

    return [len(t), r]
