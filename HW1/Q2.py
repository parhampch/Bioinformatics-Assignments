def main():
    str1 = input()
    str2 = input()
    n = len(str1)
    m = len(str2)
    str1 = '#' + str1
    str2 = '#' + str2
    gap_opening_penalty = 11
    gap_extension_penalty = 1
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
    without_gap = [[0 for i in range(m + 1)] for j in range(n + 1)]
    first_string_gap = [[0 for i in range(m + 1)] for j in range(n + 1)]
    second_string_gap = [[0 for i in range(m + 1)] for j in range(n + 1)]
    where_come_from1 = [[0 for i in range(m + 1)] for j in range(n + 1)]
    where_come_from2 = [[0 for i in range(m + 1)] for j in range(n + 1)]
    where_come_from3 = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        without_gap[i][0] = -100000
        first_string_gap[i][0] = -100000
        second_string_gap[i][0] = -gap_opening_penalty - ((i - 1) * gap_extension_penalty)
    for i in range(1, m + 1):
        without_gap[0][i] = -100000
        first_string_gap[0][i] = -gap_opening_penalty - ((i - 1) * gap_extension_penalty)
        second_string_gap[0][i] = -100000
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            temp1 = max(without_gap[i - 1][j - 1], first_string_gap[i - 1][j - 1], second_string_gap[i - 1][j - 1]) + \
                    scores[ord(str1[i]) - 65][ord(str2[j]) - 65]
            temp2 = max(without_gap[i][j - 1] - gap_opening_penalty, first_string_gap[i][j - 1] - gap_extension_penalty,
                        second_string_gap[i][j - 1] - gap_opening_penalty)
            temp3 = max(without_gap[i - 1][j] - gap_opening_penalty, first_string_gap[i - 1][j] - gap_opening_penalty,
                        second_string_gap[i - 1][j] - gap_extension_penalty)
            without_gap[i][j] = temp1
            first_string_gap[i][j] = temp2
            second_string_gap[i][j] = temp3
            if temp1 == without_gap[i - 1][j - 1] + scores[ord(str1[i]) - 65][ord(str2[j]) - 65]:
                where_come_from1[i][j] = 0
            elif temp1 == first_string_gap[i - 1][j - 1] + scores[ord(str1[i]) - 65][ord(str2[j]) - 65]:
                where_come_from1[i][j] = 1
            else:
                where_come_from1[i][j] = 2

            if temp2 == without_gap[i][j - 1] - gap_opening_penalty:
                where_come_from2[i][j] = 0
            elif temp2 == first_string_gap[i][j - 1] - gap_extension_penalty:
                where_come_from2[i][j] = 1
            else:
                where_come_from2[i][j] = 2

            if temp3 == without_gap[i - 1][j] - gap_opening_penalty:
                where_come_from3[i][j] = 0
            elif temp3 == first_string_gap[i - 1][j] - gap_opening_penalty:
                where_come_from3[i][j] = 1
            else:
                where_come_from3[i][j] = 2

    best = max(without_gap[n][m], first_string_gap[n][m], second_string_gap[n][m])
    print(best)
    if best == without_gap[n][m]:
        last_where = 0
    elif best == first_string_gap[n][m]:
        last_where = 1
    else:
        last_where = 2

    str_ans1 = ''
    str_ans2 = ''
    i = n
    j = m
    while i != 0 or j != 0:
        if last_where == 0:
            str_ans1 = str1[i] + str_ans1
            str_ans2 = str2[j] + str_ans2
            last_where = where_come_from1[i][j]
            i -= 1
            j -= 1
        elif last_where == 1:
            str_ans1 = '-' + str_ans1
            str_ans2 = str2[j] + str_ans2
            last_where = where_come_from2[i][j]
            j -= 1
        else:
            str_ans1 = str1[i] + str_ans1
            str_ans2 = '-' + str_ans2
            last_where = where_come_from3[i][j]
            i -= 1

    print(str_ans1)
    print(str_ans2)


if __name__ == '__main__':
    main()
