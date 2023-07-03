import numpy as np


def read_matrix_rows(n):
    return [list(map(int, input().split())) for _ in range(n)]


def has_same_sum(matrix):
    return len(np.unique(
        np.concatenate([matrix.sum(axis=1), matrix.sum(axis=0),
                        [matrix.diagonal().sum()], [np.fliplr(matrix).diagonal().sum()]]))) == 1


def is_magic(matrix):
    return has_same_sum(matrix) and is_valid(matrix)


def is_valid(matrix):
    return np.min(matrix) == 1 and np.max(matrix) == matrix.size\
        and len(set(matrix.flatten())) == matrix.size


def run(n):
    print('YES' if is_magic(np.array(read_matrix_rows(n))) else 'NO')


run(int(input()))
