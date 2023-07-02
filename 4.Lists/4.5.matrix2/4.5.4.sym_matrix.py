import numpy as np


def is_symmetric(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)


def read_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def run(n):
    print('YES' if is_symmetric(np.array(read_matrix_rows(n))) else 'NO')


run(int(input()))
