import numpy as np


def main():
    file = open('rosalind_ba10c.txt', 'r')
    string = file.readline().strip()
    file.readline()
    hidden_values = file.readline().strip().split()
    file.readline()
    state_values = file.readline().strip().split()
    file.readline()
    hv_mapper = {}
    for i, val in enumerate(hidden_values):
        hv_mapper[val] = i
    state_mapper = {}
    for i, val in enumerate(state_values):
        state_mapper[val] = i
    trans_matrix = np.zeros((len(state_values), len(state_values)))
    file.readline()
    for i in range(len(state_values)):
        temp = file.readline().strip().split()
        for j in range(len(state_values)):
            trans_matrix[state_mapper[temp[0]]][j] = float(temp[j + 1])
    file.readline()
    file.readline()
    em_matrix = np.zeros((len(state_values), len(hidden_values)))
    for i in range(len(state_values)):
        temp = file.readline().strip().split()
        for j in range(len(hidden_values)):
            em_matrix[state_mapper[temp[0]]][j] = float(temp[j + 1])

    viterbi = np.zeros((len(state_values), len(string)))
    parents = np.zeros((len(state_values), len(string)))
    for i in range(len(state_values)):
        viterbi[i][0] = em_matrix[i][hv_mapper[string[0]]] / len(state_values)

    for i in range(1, len(string)):
        for j in range(len(state_values)):
            temp = viterbi[:, i - 1] * trans_matrix[:, j]
            viterbi[j][i] = np.max(temp) * em_matrix[j][hv_mapper[string[i]]]
            parents[j][i] = np.argmax(temp)

    temp_max = np.argmax(viterbi[:, len(string) - 1])
    result = state_values[temp_max]
    par = len(string) - 1
    while par > 0:
        temp_max = int(parents[temp_max][par])
        par -= 1
        result = state_values[temp_max] + result
    print(result)


if __name__ == '__main__':
    main()

