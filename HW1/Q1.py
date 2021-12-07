def main(str1, str2):
    n = len(str1)
    m = len(str2)
    str1 = '#' + str1
    str2 = '#' + str2
    dp_matrix = [[0 for i in range(m + 1)] for j in range(n + 1)]
    where_come_from1 = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp_matrix[i][0] = i
        where_come_from1[i][0] = 1
    for i in range(m + 1):
        dp_matrix[0][i] = i
        where_come_from1[0][i] = 2

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            temp1 = min(dp_matrix[i - 1][j - 1] + (str1[i] != str2[j]), dp_matrix[i - 1][j] + 1, dp_matrix[i][j - 1] + 1)
            dp_matrix[i][j] = temp1
            if temp1 == dp_matrix[i - 1][j - 1] + (str1[i] != str2[j]):
                where_come_from1[i][j] = 0
            elif temp1 == dp_matrix[i - 1][j] + 1:
                where_come_from1[i][j] = 1
            else:
                where_come_from1[i][j] = 2

    best = dp_matrix[n][m]
    str_ans1 = ''
    str_ans2 = ''
    i = n
    j = m
    last_where = where_come_from1[n][m]
    while i > 0 or j > 0:
        if last_where == 0:
            str_ans1 = str1[i] + str_ans1
            str_ans2 = str2[j] + str_ans2
            i -= 1
            j -= 1
            last_where = where_come_from1[i][j]
        elif last_where == 1:
            str_ans2 = '-' + str_ans2
            str_ans1 = str1[i] + str_ans1
            i -= 1
            last_where = where_come_from1[i][j]
        else:
            str_ans2 = str2[j] + str_ans2
            str_ans1 = '-' + str_ans1
            j -= 1
            last_where = where_come_from1[i][j]
    print(best)
    print(str_ans1)
    print(str_ans2)


if __name__ == '__main__':
    file = open('rosalind_edta.txt', 'r')
    input1 = ''
    file.readline()
    temp = file.readline()
    while not(temp.startswith('>Rosalind_')):
        input1 += temp.strip()
        temp = file.readline()
    input2 = ''
    temp = file.readline()
    while temp != '':
        input2 += temp.strip(

        )
        temp = file.readline()
    main(input1, input2)
