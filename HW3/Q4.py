def neighbor_joining(matrix, n, new_node):
    if n == 2:
        return {0: [(1, matrix[0][1])], 1: [(0, matrix[0][1])]}


def main():
    file = open('rosalind_ba7c.txt', 'r')
    n = int(file.readline())
    matrix = []
    for line in file.readlines():
        matrix.append(list(map(int, line.split())))


if __name__ == '__main__':
    main()
