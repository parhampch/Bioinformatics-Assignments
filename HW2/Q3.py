def create_graph(dna_strings):
    graph = {}
    for string in dna_strings:
        str_len = len(string)
        graph[string[:str_len - 1]] = string[1:]
    return graph


def main():
    file = open('rosalind_pcov.txt', 'r')
    dna_strings = []
    for line in file.readlines():
        dna_strings.append(line.strip())
    graph = create_graph(dna_strings)
    result = dna_strings[0][:-1]
    current = graph[dna_strings[0][:-1]]
    while current != dna_strings[0][:-1]:
        result += current[-1]
        current = graph[current]
    print(result[:len(dna_strings)])


if __name__ == '__main__':
    main()
