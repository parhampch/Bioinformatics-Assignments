import numpy as np
import copy


def run_forward(string, state_values, em_matrix, trans_matrix, hv_mapper):
    forward = np.zeros((len(state_values), len(string)))
    for i in range(len(state_values)):
        forward[i][0] = em_matrix[i][hv_mapper[string[0]]] / len(state_values)

    for i in range(1, len(string)):
        for j in range(len(state_values)):
            temp = forward[:, i - 1] * trans_matrix[:, j]
            forward[j][i] = np.sum(temp) * em_matrix[j][hv_mapper[string[i]]]
    return forward


def run_backward(string, state_values, em_matrix, trans_matrix, hv_mapper):
    backward = np.ones((len(state_values), len(string)))

    string_rev = string[::-1]
    for i in range(1, len(string_rev)):
        for j in range(len(state_values)):
            temp = backward[:, i - 1] * trans_matrix[j, :] * em_matrix[:, hv_mapper[string_rev[i - 1]]]
            backward[j][i] = np.sum(temp)
    return np.flip(backward, axis=1)


def read_data(path):
    file = open(path, 'r')
    n = int(file.readline().strip())
    file.readline()
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
    return n, string, hidden_values, state_values, hv_mapper, state_mapper, trans_matrix, em_matrix


def write_data(trans_matrix, em_matrix, state_values, hidden_values, hv_mapper, state_mapper):
    temp = ''
    for val in state_values:
        temp += val + '\t'
    print(temp)
    for val in state_values:
        temp = val + '\t'
        for num in trans_matrix[state_mapper[val]]:
            temp += '{:.3f}'.format(num) + '\t'
        print(temp)
    print('-' * 8)
    temp = ''
    for val in hidden_values:
        temp += val + '\t'
    print(temp)
    for val in state_values:
        temp = val + '\t'
        for num in em_matrix[state_mapper[val]]:
            temp += '{:.3f}'.format(num) + '\t'
        print(temp)


def main():
    n, string, hidden_values, state_values, hv_mapper, state_mapper, trans_matrix, em_matrix = read_data('rosalind_ba10k.txt')
    for _ in range(n):
        forward = run_forward(string, state_values, em_matrix, trans_matrix, hv_mapper)
        backward = run_backward(string, state_values, em_matrix, trans_matrix, hv_mapper)
        trans_matrix_copy = copy.deepcopy(trans_matrix)
        em_matrix_copy = copy.deepcopy(em_matrix)
        scale_factor = forward[:, -1].sum()

        em_matrix *= 0
        for i in range(len(string)):
            for j in range(len(state_values)):
                em_matrix[j][hv_mapper[string[i]]] += forward[j][i] * backward[j][i]
        em_matrix /= scale_factor
        em_matrix /= em_matrix.sum(axis=1)[:, None]

        for i in range(len(state_values)):
            for j in range(len(state_values)):
                temp = np.array([hv_mapper[string[k]] for k in range(1, len(string))])
                trans_matrix[i][j] = (trans_matrix_copy[i][j] * (forward[i, :-1] * backward[j, 1:] * em_matrix_copy[j][temp])).sum()
        trans_matrix /= scale_factor
        trans_matrix /= trans_matrix.sum(axis=1)[:, None]
    write_data(trans_matrix, em_matrix, state_values, hidden_values, hv_mapper, state_mapper)


if __name__ == '__main__':
    main()

