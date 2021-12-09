str1 = ''
str2 = ''
str_ans1 = ''
str_ans2 = ''
scores = [
            [4,0,0,-2,-1,-2,0,-2,-1,0,-1,-1,-1,-2,0,-1,-1,-1,1,0,0,0,-3,0,-2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,9,-3,-4,-2,-3,-3,-1,0,-3,-1,-1,-3,0,-3,-3,-3,-1,-1,0,-1,-2,0,-2,0],
            [-2,0,-3,6,2,-3,-1,-1,-3,0,-1,-4,-3,1,0,-1,0,-2,0,-1,0,-3,-4,0,-3,0],
            [-1,0,-4,2,5,-3,-2,0,-3,0,1,-3,-2,0,0,-1,2,0,0,-1,0,-2,-3,0,-2,0],
            [-2,0,-2,-3,-3,6,-3,-1,0,0,-3,0,0,-3,0,-4,-3,-3,-2,-2,0,-1,1,0,3,0],
            [0,0,-3,-1,-2,-3,6,-2,-4,0,-2,-4,-3,0,0,-2,-2,-2,0,-2,0,-3,-2,0,-3,0],
            [-2,0,-3,-1,0,-1,-2,8,-3,0,-1,-3,-2,1,0,-2,0,0,-1,-2,0,-3,-2,0,2,0],
            [-1,0,-1,-3,-3,0,-4,-3,4,0,-3,2,1,-3,0,-3,-3,-3,-2,-1,0,3,-3,0,-1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [-1,0,-3,-1,1,-3,-2,-1,-3,0,5,-2,-1,0,0,-1,1,2,0,-1,0,-2,-3,0,-2,0],
            [-1,0,-1,-4,-3,0,-4,-3,2,0,-2,4,2,-3,0,-3,-2,-2,-2,-1,0,1,-2,0,-1,0],
            [-1,0,-1,-3,-2,0,-3,-2,1,0,-1,2,5,-2,0,-2,0,-1,-1,-1,0,1,-1,0,-1,0],
            [-2,0,-3,1,0,-3,0,1,-3,0,0,-3,-2,6,0,-2,0,0,1,0,0,-3,-4,0,-2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [-1,0,-3,-1,-1,-4,-2,-2,-3,0,-1,-3,-2,-2,0,7,-1,-2,-1,-1,0,-2,-4,0,-3,0],
            [-1,0,-3,0,2,-3,-2,0,-3,0,1,-2,0,0,0,-1,5,1,0,-1,0,-2,-2,0,-1,0],
            [-1,0,-3,-2,0,-3,-2,0,-3,0,2,-2,-1,0,0,-2,1,5,-1,-1,0,-3,-3,0,-2,0],
            [1,0,-1,0,0,-2,0,-1,-2,0,0,-2,-1,1,0,-1,0,-1,4,1,0,-2,-3,0,-2,0],
            [0,0,-1,-1,-1,-2,-2,-2,-1,0,-1,-1,-1,0,0,-1,-1,-1,1,5,0,0,-2,0,-2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,-1,-3,-2,-1,-3,-3,3,0,-2,1,1,-3,0,-2,-2,-3,-2,0,0,4,-3,0,-1,0],
            [-3,0,-2,-4,-3,1,-2,-2,-3,0,-3,-2,-1,-4,0,-4,-2,-3,-3,-2,0,-3,11,0,2,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [-2,0,-2,-3,-2,3,-3,2,-1,0,-2,-1,-1,-2,0,-3,-1,-2,-2,-2,0,-1,2,0,7,0],
    ]
gap_penalty = 5


def linear_space_alignment(top, bottom, left, right):
    global str_ans1
    global str_ans2
    if top == bottom:
        for i in range(left, right):
            str_ans1 += '-'
            str_ans2 += str2[i]
        return
    if left == right:
        for i in range(top, bottom):
            str_ans1 += str1[i]
            str_ans2 += '-'
        return

    middle = (left + right) // 2
    score1, path1 = find_middle_node(str1[top:bottom], str2[left:middle])
    score2, path2 = find_middle_node(str1[top:bottom][::-1], str2[middle:right][::-1])
    score2 = score2[::-1]
    path2 = path2[::-1]
    middle_node = 0
    best_score = float('-inf')
    for i in range(len(score1)):
        if score1[i] + score2[i] > best_score:
            best_score = score1[i] + score2[i]
            middle_node = i
    linear_space_alignment(top, top + middle_node, left, middle)
    middle_edge1 = path1[middle_node]
    middle_edge2 = path2[middle_node]
    if middle_edge2 == 0:
        str_ans1 += str1[top + middle_node]
        str_ans2 += str2[middle]
        middle += 1
        middle_node += 1
    elif middle_edge2 == 1:
        str_ans1 += '-'
        str_ans2 += str2[middle]
        middle += 1
    else:
        str_ans1 += str1[top + middle_node]
        str_ans2 += '-'
        middle_node += 1
    linear_space_alignment(top + middle_node, bottom, middle, right)


def find_middle_node(u, v):
    n = len(u)
    m = len(v)
    u = '#' + u
    v = '#' + v
    col1 = [-i * gap_penalty for i in range(n + 1)]
    col2 = []
    path = [2 for i in range(n + 1)]
    for i in range(1, m + 1):
        col2 = [-i * gap_penalty]
        path = [1]
        for j in range(1, n + 1):
            temp = [col1[j - 1] + scores[ord(u[j]) - 65][ord(v[i]) - 65], col1[j] - gap_penalty,
                    col2[j - 1] - gap_penalty]
            max_temp = max(temp)
            col2.append(max_temp)
            path.append(temp.index(max_temp))
        col1 = col2.copy()
    return col1, path


if __name__ == '__main__':
    file = open('rosalind_ba5l.txt', 'r')
    str1 = file.readline().strip()
    str2 = file.readline().strip()
    linear_space_alignment(0, len(str1), 0, len(str2))
    score = 0
    for i in range(len(str_ans1)):
        if str_ans1[i] == '-' or str_ans2[i] == '-':
            score -= gap_penalty
        else:
            score += scores[ord(str_ans1[i]) - 65][ord(str_ans2[i]) - 65]
    print(score)
    print(str_ans1)
    print(str_ans2)
