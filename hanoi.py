def hanoi(n, a, b, c):
    if n == 1:
        return [[a, c]]
    return hanoi(n-1, a, c, b) + [[a, c]] + hanoi(n-1, b, a, c)


if __name__ == "__main__":
    print(hanoi(3, 1, 2, 3))
