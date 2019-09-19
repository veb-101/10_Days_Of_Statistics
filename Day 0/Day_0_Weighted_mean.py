# length = int(input())
# array = input()
# weights = input()

length = 5
array = '10 40 30 50 20'
weights = '1 2 3 4 5'

array = list(map(int, array.split()))
weights = list(map(int, weights.split()))

total = 0
for i, j in zip(array, weights):
    total += i*j

print(round(total/sum(weights), 1))
