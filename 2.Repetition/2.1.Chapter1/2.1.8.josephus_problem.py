def solve_joseph(person, k, index):
    # Base case , when only one person is left
    if len(person) == 1:
        return person[0]

    # find the index of first person which will die
    index = ((index + k) % len(person))

    # remove the first person which is going to be killed
    person.pop(index)

    # recursive call for n-1 persons
    solve_joseph(person, k, index)


def run(n, k):
    print(solve_joseph(list(range(n)), k, 0))


run(*map(int, [input() for _ in range(2)]))
