def main(str1, str2):
    n = len(str1)
    m = len(str2)
    str1 = '#' + str1
    str2 = '#' + str2
    dp_matrix = [[0 for i in range(n + 1)] for j in range(m + 1)]
    where_come_from1 = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        dp_matrix[i][0] = -i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            temp = max(dp_matrix[i - 1][j - 1] + [-1, 1][str1[j] == str2[i]], dp_matrix[i][j - 1] - 1,
                                  dp_matrix[i - 1][j] - 1)
            dp_matrix[i][j] = temp
            if temp == dp_matrix[i - 1][j] - 1:
                where_come_from1[i][j] = 0
            elif temp == dp_matrix[i][j - 1] - 1:
                where_come_from1[i][j] = 1
            else:
                where_come_from1[i][j] = 2

    best = max(dp_matrix[m])
    print(best)
    i = m
    j = dp_matrix[m].index(best)
    last_where = where_come_from1[i][j]
    res_ans1 = ''
    res_ans2 = ''
    while i > 0:
        if last_where == 0:
            res_ans2 = str2[i] + res_ans2
            res_ans1 = '-' + res_ans1
            i -= 1
        elif last_where == 1:
            res_ans2 = '-' + res_ans2
            res_ans1 = str1[j] + res_ans1
            j -= 1
        else:
            res_ans2 = str2[i] + res_ans2
            res_ans1 = str1[j] + res_ans1
            j -= 1
            i -= 1
        last_where = where_come_from1[i][j]
    print(res_ans1)
    print(res_ans2)


if __name__ == '__main__':
    file = open('rosalind_sims.txt', 'r')
    input1 = ''
    file.readline()
    temp = file.readline()
    while not(temp.startswith('>Rosalind_')):
        input1 += temp.strip()
        temp = file.readline()
    input2 = ''
    temp = file.readline()
    while temp != '':
        input2 += temp.strip()
        temp = file.readline()
    main(input1, input2)