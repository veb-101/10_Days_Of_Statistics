a = []
for i in range(1, 7):
    for j in range(1, 7):
        a.append((i, j))

total = 0

for i, j in a:
    if i != j and i + j == 6:
        total += 1

print(f"Probablity = {total/ len(a)}")
