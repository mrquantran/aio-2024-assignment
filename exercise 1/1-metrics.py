from support import isNumber, isGreaterThan0

@isNumber
@isGreaterThan0
def precision(tp, fp):
    return tp / (tp + fp)


@isNumber
@isGreaterThan0
def recall(tp, fn):
    return tp / (tp + fn)


@isNumber
@isGreaterThan0
def f1_score(tp, fp, fn):
    p = precision(tp, fp)
    r = recall(tp, fn)
    return 2 * p * r / (p + r)


@isNumber
@isGreaterThan0
def evalute_metrics(tp, fp, fn) -> tuple:
    p = precision(tp, fp)
    r = recall(tp, fn)
    f1 = f1_score(tp, fp, fn)
    return p, r, f1

precision, recall, f1_score = evalute_metrics(tp=2, fp=3, fn=4)
print(f'Precision: {precision}, Recall: {recall}, F1 Score: {f1_score}')

# evalute_metrics(tp=-3, fp=-3, fn=4)
# evalute_metrics(tp=2, fp=-3, fn=4)