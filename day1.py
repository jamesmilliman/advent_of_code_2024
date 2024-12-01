def silver():
    a = list()
    b = list()
    with open('day1.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            a.append(int(line[0]))
            b.append(int(line[1]))
    
    a.sort()
    b.sort()

    ret = 0
    for an, bn in zip(a, b):
        ret += abs(an - bn)
    return ret


def gold():
    a = list()
    b = list()
    with open('day1.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            a.append(int(line[0]))
            b.append(int(line[1]))
    
    counts = dict()
    for each in b:
        if each not in counts:
            counts[each] = 0
        counts[each] += 1

    ret = 0
    for an in a:
        bvalue = 0 if an not in counts else counts[an]
        ret += bvalue * an
    return ret


if __name__ == "__main__":
    print(silver())
    print(gold())
