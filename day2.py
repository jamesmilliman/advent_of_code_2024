import math


def silver():
    with open("day2.txt") as f:
        lines = f.readlines()
        lines = [list(map(lambda x: int(x), line.strip().split(" "))) for line in lines]

    ret = 0
    for line in lines:
        deltas = list()
        for i in range(len(line) - 1):
            deltas.append(line[i] - line[i + 1])
        ads = [abs(d) for d in deltas]
        ret += int(
            (all(map(lambda x: x < 0, deltas)) or all(map(lambda x: x > 0, deltas)))
            and max(ads) < 4
        )
    return ret


def gold():
    from copy import deepcopy

    with open("day2.txt") as f:
        lines = f.readlines()
        lines = [list(map(lambda x: int(x), line.strip().split(" "))) for line in lines]

    ret = 0
    for line in lines:
        ops = list()
        cur = list()

        def helper(line, i, passed):
            if i == len(line):
                ops.append(deepcopy(cur))
                return

            if passed:
                cur.append(line[i])
                helper(line, i + 1, passed)
                cur.pop()
            else:
                cur.append(line[i])
                helper(line, i + 1, passed)
                cur.pop()
                helper(line, i + 1, True)

        helper(line, 0, False)
        for option in ops:
            deltas = list()
            for i in range(len(option) - 1):
                deltas.append(option[i] - option[i + 1])
            ads = [abs(d) for d in deltas]
            value = (
                all(map(lambda x: x < 0, deltas)) or all(map(lambda x: x > 0, deltas))
            ) and max(ads) < 4
            ret += int(value)
            if value:
                break

    return ret


if __name__ == "__main__":
    print(silver())
    print(gold())
