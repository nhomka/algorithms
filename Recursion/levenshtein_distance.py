from operator import le


def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    d = range(len(s1) + 1)

    for i2, c2 in enumerate(s2):
        d_ = [i2 + 1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                d_.append(d[i1])
            else:
                d_.append(1 + min(d[i1], d[i1 + 1], d_[i1-1]))
        d = d_
    return d[-1]

print(levenshtein_distance("edcba", "bcd"))