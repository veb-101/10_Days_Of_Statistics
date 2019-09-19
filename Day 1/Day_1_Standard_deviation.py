length = 5
array = '10 40 30 50 20'

array = list(map(int, array.split()))


def mean(a):
    return sum(a)/len(a)


def std_dev(array, length):
    mu = mean(array)
    total = 0
    for i in array:
        total += (i - mu) ** 2
    return round((total / length) ** .5, 1)

print(std_dev(array, length))
