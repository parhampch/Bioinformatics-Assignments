from queue import Queue


def bfs(tree, node):
    dist = [-1 for i in range(len(tree))]
    u = node
    dist[u] = 0
    q = Queue()
    for v, w in tree[u]:
        q.put(v)
        dist[v] = dist[u] + w

    while not(q.empty()):
        u = q.get()
        for v, w in tree[u]:
            if dist[v] == -1:
                q.put(v)
                dist[v] = dist[u] + w
    return dist


def find_distances(n, tree):
    matrix = []
    for i in range(n):
        matrix.append(bfs(tree, i)[:n])
    return matrix


def main():
    file = open('rosalind_ba7a.txt', 'r')
    n = int(file.readline())
    tree = {}
    for line in file.readlines():
        u, rest = line.split('->')
        v, w = rest.split(':')
        u, v, w = int(u), int(v), int(w)
        if not(tree.__contains__(u)):
            tree[u] = []
        tree[u].append((v, w))
    matrix = find_distances(n, tree)
    for i in range(n):
        temp = ''
        for j in range(n):
            temp += str(matrix[i][j]) + ' '
        print(temp)


if __name__ == '__main__':
    main()

