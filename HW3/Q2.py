def find_limb_length(n, j, matrix):
    ans = float('inf')
    for i in range(n):
        for k in range(n):
            if (i == j) or (i == k) or (j == k):
                continue
            ans = min(ans, (matrix[j][i] + matrix[j][k] - matrix[i][k]) / 2)
    return int(ans)


def main():
    file = open('rosalind_ba7b.txt', 'r')
    n = int(file.readline())
    j = int(file.readline())
    matrix = []
    for line in file.readlines():
        matrix.append(list(map(int, line.split())))
    print(find_limb_length(n, j, matrix))


if __name__ == '__main__':
    main()



