import random


def getf(a):
    f = []
    for i in range(len(a)):
        f.append(a[i][i])
    return f


def getGrad(f):
    gr = []
    for i in f:
        gr.append(2 * i)
    return gr


def displayf(f):
    print(f[0], '*x_0', '^2', sep='', end='')
    for i in range(1, len(f)):
        print(' + ', f[i], "*x_", i, '^2', sep='', end='')


def quadraticFuncGenerator(n, k):
    a = [[0] * n for _ in range(n)]

    firstInd = random.randint(0, n - 1)
    secondInd = random.randint(0, n - 1)

    if n != 1:
        while firstInd == secondInd:
            secondInd = random.randint(0, n - 1)
        a[firstInd][firstInd] = k
        a[secondInd][secondInd] = 1
    else:
        a[firstInd][firstInd] = k

    for i in range(n):
        if i == firstInd or i == secondInd:
            continue
        a[i][i] = random.randint(1, k)
    return a


def main():
    n, k = map(int, input().split())
    matrix = quadraticFuncGenerator(n, k)
    f = getf(matrix)
    displayf(f)
    gr = getGrad(f)
    print()
    print(gr)


if __name__ == '__main__':
    main()
