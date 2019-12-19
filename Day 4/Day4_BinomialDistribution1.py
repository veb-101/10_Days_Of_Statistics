from math import factorial as f

n = 6
l, r = list(map(float, input().split()))
odds = l / r
p = odds / (1 + odds)
q = 1 - p


def combi(n, x):
    return f(n) / (f(x) * f(n-x))


def binomial(x, n, p):
    return combi(n, x) * p ** x * q ** (n - x)

print(round(sum([binomial(i, n, p) for i in range(3, 7)]), 3))