# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from random import *
from math import *
import time


class Der:
    def __init__(self, sa, sb):
        self.a = sa
        self.b = sb
        self.url_inp = []
        self.url_out = 0


def requrs(der, ind, flag):
    der[ind].b += 1
    der[ind].a += flag
    if ind == 0:
        return 0
    else:
        return requrs(der, der[ind].url_out, flag)


def prow(der, ind, kol, c):
    if len(der[ind].url_inp) == 0:
        return ind
    else:
        ma = -10000000
        mai = 0
        for i in der[ind].url_inp:
            x = der[i].a / der[i].b + c * sqrt((2 * log(kol)) / der[i].b)
            if x >= ma:
                ma = x
                mai = i
        return prow(der, mai, kol, c)


def Game(otw, mai):
    return uniform(otw[mai], 1)


def Run(otw, j):
    # мы считаем корень первой игро, но это не так
    n_kol = len(otw)
    koren = 0
    der = [Der(0, 0)]
    ind = 0
    for i in range(n_kol):
        a = uniform(otw[i], 1)
        der[ind].url_inp.append(len(der))
        der.append(Der(round(a), 1))
        der[-1].url_out = ind
        requrs(der, der[-1].url_out, round(a))
    kol = n_kol
    c = 1 / j
    epochs = int(5000 * (1 / c))
    mai = 0
    for epoch in range(epochs):
        ind = prow(der, 0, kol, c)
        # опредляем како1 атомат
        ma = -10000000
        mai = 0
        for i in der[koren].url_inp:
            x = der[i].a / der[i].b + c * sqrt((2 * log(kol)) / der[i].b)
            if x >= ma:
                ma = x
                mai = i
        mai -= 1
        # -----------------------------------------------------------
        a = Game(otw, mai)
        der[ind].url_inp.append(len(der))
        der.append(Der(round(a), 1))
        der[-1].url_out = ind
        requrs(der, der[-1].url_out, round(a))
        kol += 1
    return mai


def Test(j):
    # n_kol>=2
    n_kol = 10
    koren = 0
    otw = [uniform(0, 1) for i in range(n_kol)]
    mai = Run(otw, j)
    # print(*otw)
    # print(max(otw), otw.index(max(otw)))
    # print(mai)
    if mai == otw.index(max(otw)):
        return 1
    else:
        return 0


def print_hi(name):
    tim = time.time()
    k = 10
    for j in range(1, k + 2):
        n = 100
        kol = 0
        for i in range(n):
            kol += Test(j)
        print(j / k, kol / n * 100)
    print(time.time() - tim)


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 8)
    print_hi('PyCharm')
