from math import factorial as f

p, n = list(map(int, input().split()))
p = p / 100
q = 1 - p


def combi(n, x):
    return f(n) / (f(x) * f(n-x))


def binomial(x, n, p):
    return combi(n, x) * p ** x * q ** (n - x)


print(round(sum([binomial(i, n, p) for i in range(3)]), 3))
print(round(sum([binomial(i, n, p) for i in range(2, n + 1)]), 3))
