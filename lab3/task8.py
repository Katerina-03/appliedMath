import numpy as np
import task7 as gn
import random
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (10, 10)

function = np.array([])
gradient = np.array([])


def f(X):
    return np.dot(function, np.power(X, 2))


def grad(X):
    return gradient * X


def get_fun(n, k):
    mtr = gn.quadraticFuncGenerator(n, k)
    func = gn.getf(mtr)
    return np.array(func)


def random_start(n):
    return [random.randint(0, 20) for _ in range(n)]


def golden_search(x0, eps):
    a = 0
    b = 1
    while abs(a - b) / 2 > eps:
        lr1, lr2 = (a + b - eps) / 2, (a + b + eps) / 2
        x1 = x0 - lr1 * grad(x0)
        x2 = x0 - lr2 * grad(x0)
        if f(x1) < f(x2):
            b = lr2
        else:
            a = lr1
    return (a + b) / 2


def steepest_descent(x0, eps):
    x = np.array(x0)
    i = 1
    while True:
        lr = golden_search(x, eps)
        x1 = x - lr * grad(x)
        if np.linalg.norm(x1 - x) < eps or i > 1e4:
            return i
        x = x1
        i += 1


def count_of_iterations(ps):
    return steepest_descent(ps, 0.0001)


def draw(t, count_for_n):
    global function, gradient
    if count_for_n:
        label = "Размерность пространства"
        log = "n = "
    else:
        label = "Число обусловленности"
        log = "k = "
    launches = 10
    sum = np.array([0] * 1001)
    for _ in range(launches):
        vals = np.array([0] * 1001)
        for q in range(1, 1001):
            if count_for_n:
                function = get_fun(q, t)
                loc_start = random_start(q)
            else:
                function = get_fun(t, q)
                loc_start = random_start(t)
            gradient = function * 2
            c = count_of_iterations(loc_start)
            vals[q] = c
            print(log, q, "done")
        sum += vals
    res = sum / launches
    plt.xlabel(label)
    plt.ylabel("Число итераций")
    plt.plot(res)
    plt.show()


if __name__ == '__main__':
    draw(2, False)
