def find_dist(string, seq):
    min_dist = float('inf')
    for i in range(len(string) - len(seq)):
        temp = 0
        for j in range(len(seq)):
            temp += seq[j] != string[j + i]
        if temp < min_dist:
            min_dist = temp
    return min_dist


def main():
    file = open('rosalind_ba2b (1).txt', 'r')
    n = int(file.readline())
    strings = []
    for line in file.readlines():
        strings.append(line)
    letters = ['A', 'C', 'G', 'T']
    all_seq = ['A', 'C', 'G', 'T']
    for i in range(n - 1):
        all_seq = [j + k for j in all_seq for k in letters]
    min_seq = ''
    min_score = float('inf')
    for seq in all_seq:
        temp = 0
        for string in strings:
            temp += find_dist(string, seq)
        if temp < min_score:
            min_score = temp
            min_seq = seq
    print(min_seq)


if __name__ == '__main__':
    main()

