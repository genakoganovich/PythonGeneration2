def get_sublist(lst, n):
    return [lst[i:(i + n)] for i in range(0, len(lst), 1) if len(lst[i:(i + n)]) == n]


def get_sublist_all(lst):
    result = [[]]
    for i in range(len(lst) + 1):
        result.extend(get_sublist(lst, i))
    return result


print(get_sublist_all(input().split()))
