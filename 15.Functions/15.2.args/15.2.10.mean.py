import statistics as st


def mean(*args):
    num = list(filter(lambda x: type(x) in [int, float], args))
    return float(0) if not num else float(st.mean(num))
