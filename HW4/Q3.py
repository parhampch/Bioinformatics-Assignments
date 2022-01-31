import numpy as np


def get_profile(motifs):
    k = len(motifs[0])
    t = len(motifs)
    mapper = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    profile = np.zeros((4, k))
    for motif in motifs:
        for i in range(k):
            profile[mapper[motif[i]]][i] += 1
    profile = (profile + 1) / (t + 4)
    return profile


def get_dist_of_motifs(motifs):
    prof = get_profile(motifs)
    min_indexes = np.argmax(prof, axis=0)
    letters = ['A', 'C', 'G', 'T']
    best_motif = ''.join([letters[i] for i in min_indexes])
    dist = 0
    for motif in motifs:
        dist += find_dist(motif, best_motif)
    return dist


def get_prob(seq, profile):
    mapper = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    res = 1
    for i in range(len(seq)):
        res *= profile[mapper[seq[i]]][i]
    return res


def get_most_prob(string, profile, k):
    best_seq = string[:k]
    best_prob = 0
    for i in range(k, len(string) - k + 1):
        temp = get_prob(string[i:i + k], profile)
        if best_prob < temp:
            best_prob = temp
            best_seq = string[i:i + k]
    return best_seq


def find_dist(string1, string2):
    temp = 0
    for i in range(len(string1)):
        temp += string1[i] != string2[i]
    return temp


def main():
    file = open('rosalind_ba2f (6).txt', 'r')
    k, t = file.readline().split()
    k, t = int(k), int(t)
    strings = []
    for line in file.readlines():
        strings.append(line.strip())
    final_best_dist = float('inf')
    final_best = None
    for _ in range(1000):
        result = []
        for i in range(t):
            index = np.random.randint(len(strings[i]) - k + 1)
            result.append(strings[i][index:index + k])
        best_dist = get_dist_of_motifs(result)
        while True:
            prof = get_profile(result)
            temp = []
            for i in range(t):
                temp.append(get_most_prob(strings[i], prof, k))
            temp_dist = get_dist_of_motifs(temp)
            if temp_dist < best_dist:
                result = temp
                best_dist = temp_dist
            else:
                break
        if best_dist < final_best_dist:
            final_best_dist = best_dist
            final_best = result
    for s in final_best:
        print(s)


if __name__ == '__main__':
    main()

