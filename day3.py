def one():
    with open("day3.txt") as f:
        text = "".join(f.readlines())

    def try_parse(i):
        if text[i] != "(":
            return None, i
        i += 1
        left = None
        cur = 0
        while i < len(text):
            ch = text[i]
            if ch.isdigit():
                cur = cur * 10 + int(ch)
            else:
                if ch == "," and cur > 0 and left is None:
                    left = cur
                    cur = 0
                elif ch == ")" and cur > 0 and left is not None:
                    return (left, cur), i + 1
                else:
                    return None, i
            i += 1
        return None, i

    i = 0
    prod = 0
    while i < len(text) - 3:
        if text[i] == "m" and text[i + 1] == "u" and text[i + 2] == "l":
            ret, i = try_parse(i + 3)
            if ret is not None:
                prod += ret[0] * ret[1]
        else:
            i += 1
    return prod


def two():
    with open("day3.txt") as f:
        text = "".join(f.readlines())

    def try_parse(i):
        if text[i] != "(":
            return None, i
        i += 1
        left = None
        cur = 0
        while i < len(text):
            ch = text[i]
            if ch.isdigit():
                cur = cur * 10 + int(ch)
            else:
                if ch == "," and cur > 0 and left is None:
                    left = cur
                    cur = 0
                elif ch == ")" and cur > 0 and left is not None:
                    return (left, cur), i + 1
                else:
                    return None, i
            i += 1
        return None, i

    i = 0
    prod = 0
    enabled = True
    while i < len(text) - 3:
        if enabled and text[i] == "m" and text[i + 1] == "u" and text[i + 2] == "l":
            ret, i = try_parse(i + 3)
            if ret is not None:
                prod += ret[0] * ret[1]
        elif (
            i < len(text) - 6
            and text[i] == "d"
            and text[i + 1] == "o"
            and text[i + 2] == "n"
            and text[i + 3] == "'"
            and text[i + 4] == "t"
            and text[i + 5] == "("
            and text[i + 6] == ")"
        ):
            enabled = False
            i += 6
        elif (
            i < len(text) - 4
            and text[i] == "d"
            and text[i + 1] == "o"
            and text[i + 2] == "("
            and text[i + 3] == ")"
        ):
            enabled = True
            i += 4
        else:
            i += 1
    return prod


if __name__ == "__main__":
    print(one())
    print(two())
