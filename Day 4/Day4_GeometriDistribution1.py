p = input().split()  # 1 3
p = list(map(int, p))  # 5
n = int(input())

p = p[0] / p[1]
q = 1 - p
print(round(q ** (n-1) * p, 3))
