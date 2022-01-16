
def main():
    file = open('rosalind_asmq.txt', 'r')
    sum_length = 0
    all_length = []
    for line in file.readlines():
        sum_length += len(line.strip())
        all_length.append(len(line.strip()))
    all_length = list(reversed(sorted(all_length)))
    temp = 0
    number1 = 0
    number2 = 0
    for length in all_length:
        temp += length
        if number1 == 0 and (temp / sum_length) >= 0.5:
            number1 = length
        if (temp / sum_length) >= 0.75:
            number2 = length
            break
    print(number1, number2)


if __name__ == '__main__':
    main()
