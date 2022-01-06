import copy
def find_closest_clusters(matrix):
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


def upgma(matrix, n):
    new_node = n
    dict_matrix = {}
    tree = {}
    age = {}
    clusters = {}
    for i in range(n):
        tree[i] = []
        age[i] = 0
        clusters[i] = 1
    for i in range(n):
        dict_matrix[i] = {}
        for j in range(n):
            dict_matrix[i][j] = matrix[i][j]
    while len(clusters) > 1:

        i_min, j_min, min_dis = find_closest_clusters(dict_matrix)
        age[new_node] = min_dis / 2
        tree[new_node] = [(i_min, age[new_node] - age[i_min]), (j_min, age[new_node] - age[j_min])]
        tree[i_min].append((new_node, age[new_node] - age[i_min]))
        tree[j_min].append((new_node, age[new_node] - age[j_min]))
        clusters[new_node] = clusters[i_min] + clusters[j_min]
        dict_matrix_copy = copy.deepcopy(dict_matrix)
        dict_matrix[new_node] = {}
        for i in dict_matrix_copy:
            if i == i_min or i == j_min:
                continue
            new_dist = ((dict_matrix[i][i_min] * clusters[i_min]) + dict_matrix[i][j_min] * clusters[j_min]) / (clusters[i_min] + clusters[j_min])
            dict_matrix[i][new_node] = new_dist
            dict_matrix[new_node][i] = new_dist

            del dict_matrix[i][i_min]
            del dict_matrix[i][j_min]
        del clusters[i_min]
        del clusters[j_min]
        del dict_matrix[i_min]
        del dict_matrix[j_min]
        new_node += 1

    return tree


def main():
    file = open('rosalind_ba7d.txt', 'r')
    n = int(file.readline())
    matrix = []
    for line in file.readlines():
        matrix.append(list(map(int, line.split())))
    tree = upgma(matrix, n)
    keys = sorted(tree)
    for key in keys:
        for neighbor in sorted(tree[key]):
            print(str(key) + '->' + str(neighbor[0]) + ':' + '{:.3f}'.format(neighbor[1]))


if __name__ == '__main__':
    main()
