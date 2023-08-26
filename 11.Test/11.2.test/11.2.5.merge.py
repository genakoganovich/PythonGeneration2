def merge(values):
    res = {}
    for d in values:
        for k, v in d.items():
            res.setdefault(k, set()).add(v)
    return res
