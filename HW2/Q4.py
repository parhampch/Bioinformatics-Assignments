def mapper(string):
    result = ''
    map_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for char in string:
        result += map_dict[char]
    return result[::-1]


def find_closest(dna_strings, string):
    for s in dna_strings:
        diff = 0
        for i in range(len(string)):
            if s[i] != string[i]:
                diff += 1
        if diff == 1 and dna_strings.count(s) >= 2:
            return s
    return -1


def main():
    file = open('rosalind_corr.txt', 'r')
    dna_strings = []
    dna_strings_rc = []
    for line in file.readlines():
        if not('Rosalind' in line):
            dna_strings.append(line.strip())
            dna_strings_rc.append(mapper(line.strip()))
    all_strings = dna_strings + dna_strings_rc
    for i in range(len(dna_strings)):
        if all_strings.count(dna_strings_rc[i]) >= 2:
            continue
        corrected = find_closest(all_strings, dna_strings[i])
        print(dna_strings[i] + '->' + corrected)


if __name__ == '__main__':
    main()
