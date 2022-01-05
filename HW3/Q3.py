def find_limb_length(n, j, matrix):
    ans = float('inf')
    for i in range(n):
        for k in range(n):
            if (i == j) or (i == k) or (j == k):
                continue
            ans = min(ans, (matrix[j][i] + matrix[j][k] - matrix[i][k]) / 2)
    return int(ans)


def bfs(tree, node1, node2, visited):
    u = node1
    visited[u] = True
    for v, w in tree[u]:
        if visited[v]:
            continue
        if v == node2:
            return [(node1, w), (node2, 0)]
        rest_path = bfs(tree, v, node2, visited)
        if rest_path is not None:
            return [(node1, w)] + rest_path
    return None


def additive_phylogeny(matrix, n, new_node):
    if n == 2:
        return {0: [(1, matrix[0][1])], 1: [(0, matrix[0][1])]}
    limb_length = find_limb_length(n, n - 1, matrix)
    for i in range(n-1):
        matrix[i][n - 1] -= limb_length
        matrix[n - 1][i] = matrix[i][n - 1]

    ii, jj = -1, -1
    for i in range(n - 1):
        for j in range(n - 1):
            if i != j and matrix[i][j] == matrix[i][n-1] + matrix[j][n-1]:
                ii, jj = i, j
                break
    x = matrix[ii][n - 1]
    tree = additive_phylogeny(matrix, n - 1, new_node - 1)
    path = bfs(tree, ii, jj, [False for i in range(2 * len(matrix))])
    remain_dist = x
    index = 0
    while remain_dist >= path[index][1]:
        remain_dist -= path[index][1]
        index += 1

    tree[path[index][0]].append((new_node, remain_dist))
    tree[path[index + 1][0]].append((new_node, path[index][1] - remain_dist))
    tree[new_node] = [(path[index][0], remain_dist), (path[index + 1][0], path[index][1] - remain_dist)]
    tree[path[index][0]].remove((path[index + 1][0], path[index][1]))
    tree[path[index + 1][0]].remove((path[index][0], path[index][1]))
    tree[new_node].append((n - 1, limb_length))
    tree[n - 1] = [(new_node, limb_length)]

    return tree


def main():
    file = open('rosalind_ba7c.txt', 'r')
    n = int(file.readline())
    matrix = []
    for line in file.readlines():
        matrix.append(list(map(int, line.split())))
    tree = additive_phylogeny(matrix, n, 2 * len(matrix) - 3)
    keys = sorted(tree)
    for key in keys:
        for neighbor in sorted(tree[key]):
            print(str(key) + '->' + str(neighbor[0]) + ':' + str(neighbor[1]))


if __name__ == '__main__':
    main()
