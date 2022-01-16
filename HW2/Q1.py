def mapper(string):
    result = ''
    map_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for char in string:
        result += map_dict[char]
    return result[::-1]


def main():
    file = open('rosalind_dbru.txt', 'r')
    dna_strings = set()
    for line in file.readlines():
        dna_strings.add(line.strip())
        dna_strings.add(mapper(line.strip()))
    for string in dna_strings:
        str_len = len(string)
        print('(' + string[:str_len - 1 ] + ', ' + string[1:] + ')')


if __name__ == '__main__':
    main()
