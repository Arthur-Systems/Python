# make a generator
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def nqueens(data):
    allperms = all_perms(data)
    queens = []
    for i in allperms:
        if i[1] - i[0] != 1 and i[1] - i[0] != -1 and i[2] - i[1] != 1 and i[2] - i[1] != -1 and i[3] - i[2] != 1 and i[3] - i[2] != -1:
            queens.append(i)
    queens = queens[::-1]
    return queens


if __name__ == '__main__':
    data = [1, 2, 3, 4]  # board size
    # get the number of queens
    queens = int(input("Enter a number of queens \n"))
    if queens > len(data):
        print("Number of queens is too large")
    print(f"The {queens}-queens puzzle has {len(list(nqueens(data)))} solutions:")
    for i in nqueens(data):
        print(i)
