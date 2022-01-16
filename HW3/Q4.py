import copy
def find_total_distance(matrix):
    res = {}
    for i in matrix:
        temp_sum = 0
        for j in matrix[i]:
            temp_sum += matrix[i][j]
        res[i] = temp_sum
    return res


def find_min_of_matrix(matrix):
    min_dis = float('inf')
    ii = -1
    jj = -1
    for i in matrix:
        for j in matrix[i]:
            if i == j:
                continue
            if matrix[i][j] < min_dis:
                min_dis = matrix[i][j]
                ii = i
                jj = j
    return ii, jj, min_dis


def neighbor_joining(matrix, n, new_node):
    if n == 2:
        tree = {}
        for i in matrix:
            for j in matrix[i]:
                tree[i] = [(j, matrix[i][j])]
        return tree
    total_distance = find_total_distance(matrix)
    d_prime = {}
    for i in matrix:
        d_prime[i] = {}
        for j in matrix[i]:
            d_prime[i][j] = ((n - 2) * matrix[i][j]) - total_distance[i] - total_distance[j]
    min_i, min_j, min_val = find_min_of_matrix(d_prime)
    delta = (total_distance[min_i] - total_distance[min_j]) / (n - 2)
    limb_length_i = (matrix[min_i][min_j] + delta) / 2
    limb_length_j = (matrix[min_i][min_j] - delta) / 2
    dict_matrix_copy = copy.deepcopy(matrix)
    matrix[new_node] = {}
    for i in dict_matrix_copy:
        if i == min_i or i == min_j:
            continue
        new_dist = (matrix[i][min_i] + matrix[i][min_j] - matrix[min_i][min_j]) / 2
        matrix[i][new_node] = new_dist
        matrix[new_node][i] = new_dist

        del matrix[i][min_i]
        del matrix[i][min_j]
    del matrix[min_i]
    del matrix[min_j]
    tree = neighbor_joining(matrix, n - 1, new_node + 1)
    tree[new_node].append((min_i, limb_length_i))
    tree[new_node].append((min_j, limb_length_j))
    tree[min_i] = [(new_node, limb_length_i)]
    tree[min_j] = [(new_node, limb_length_j)]
    return tree


def main():
    file = open('sample.txt', 'r')
    n = int(file.readline())
    matrix = []
    for line in file.readlines():
        matrix.append(list(map(int, line.split())))
    dict_matrix = {}
    for i in range(n):
        dict_matrix[i] = {}
        for j in range(n):
            dict_matrix[i][j] = matrix[i][j]
    tree = neighbor_joining(dict_matrix, n, n)
    keys = sorted(tree)
    for key in keys:
        for neighbor in sorted(tree[key]):
            print(str(key) + '->' + str(neighbor[0]) + ':' + '{:.3f}'.format(neighbor[1]))


if __name__ == '__main__':
    main()
