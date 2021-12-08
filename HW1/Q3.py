def main(str1, str2):
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
    main_dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    without_gap = [[0 for i in range(m + 1)] for j in range(n + 1)]
    first_string_gap = [[0 for i in range(m + 1)] for j in range(n + 1)]
    second_string_gap = [[0 for i in range(m + 1)] for j in range(n + 1)]
    where_come_from1 = [[-1 for i in range(m + 1)] for j in range(n + 1)]
    where_come_from2 = [[-1 for i in range(m + 1)] for j in range(n + 1)]
    where_come_from3 = [[-1 for i in range(m + 1)] for j in range(n + 1)]
    best = (0, (0, 0))
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            temp1 = max(max(without_gap[i - 1][j - 1], first_string_gap[i - 1][j - 1],
                            second_string_gap[i - 1][j - 1]) + scores[ord(str1[i]) - 65][ord(str2[j]) - 65], 0)
            temp2 = max(without_gap[i][j - 1] - gap_opening_penalty, first_string_gap[i][j - 1] - gap_extension_penalty,
                        second_string_gap[i][j - 1] - gap_opening_penalty)
            temp3 = max(without_gap[i - 1][j] - gap_opening_penalty, first_string_gap[i - 1][j] - gap_opening_penalty,
                        second_string_gap[i - 1][j] - gap_extension_penalty)
            without_gap[i][j] = temp1
            first_string_gap[i][j] = temp2
            second_string_gap[i][j] = temp3
            temp4 = max(temp1, temp2, temp3)
            main_dp[i][j] = temp4
            best = max(best, (temp4, (i, j)))
            if temp4 == 0:
                where_come_from1[i][j] = -1
            elif temp1 == without_gap[i - 1][j - 1] + scores[ord(str1[i]) - 65][ord(str2[j]) - 65]:
                where_come_from1[i][j] = 0
            elif temp1 == first_string_gap[i - 1][j - 1] + scores[ord(str1[i]) - 65][ord(str2[j]) - 65]:
                where_come_from1[i][j] = 1
            else:
                where_come_from1[i][j] = 2

            if temp4 == 0:
                where_come_from2[i][j] = -1
            elif temp2 == without_gap[i][j - 1] - gap_opening_penalty:
                where_come_from2[i][j] = 0
            elif temp2 == first_string_gap[i][j - 1] - gap_extension_penalty:
                where_come_from2[i][j] = 1
            else:
                where_come_from2[i][j] = 2

            if temp4 == 0:
                where_come_from3[i][j] = -1
            elif temp3 == without_gap[i - 1][j] - gap_opening_penalty:
                where_come_from3[i][j] = 0
            elif temp3 == first_string_gap[i - 1][j] - gap_opening_penalty:
                where_come_from3[i][j] = 1
            else:
                where_come_from3[i][j] = 2

    print(best[0])
    i = best[1][0]
    j = best[1][1]
    if best[0] == without_gap[i][j]:
        last_where = 0
    elif best[0] == first_string_gap[i][j]:
        last_where = 1
    elif best[0] == second_string_gap[i][j]:
        last_where = 2
    else:
        last_where = -1

    str_ans1 = ''
    str_ans2 = ''
    while i != 0 or j != 0:
        if last_where == -1:
            break
        if last_where == 0:
            str_ans1 = str1[i] + str_ans1
            str_ans2 = str2[j] + str_ans2
            i -= 1
            j -= 1
            last_where = where_come_from1[i][j]
        elif last_where == 1:
            str_ans2 = str2[j] + str_ans2
            j -= 1
            last_where = where_come_from2[i][j]
        else:
            str_ans1 = str1[i] + str_ans1
            i -= 1
            last_where = where_come_from3[i][j]

    print(str_ans1)
    print(str_ans2)


if __name__ == '__main__':
    file = open('rosalind_laff (1).txt', 'r')
    input1 = ''
    file.readline()
    temp = file.readline()
    while not (temp.startswith('>Rosalind_')):
        input1 += temp.strip()
        temp = file.readline()
    input2 = ''
    temp = file.readline()
    while temp != '':
        input2 += temp.strip(

        )
        temp = file.readline()
    main(input1, input2)
