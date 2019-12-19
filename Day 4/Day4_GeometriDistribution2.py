p = input().split()  # 1 3
p = list(map(int, p))  
n = int(input())  # 5

p = p[0] / p[1]
q = 1 - p


prob = 1 - q ** n
print(round(prob, 3))

# prob = 0

# for i in range(n):
#     prob += (p * q ** i)

# print(round(prob, 3))
