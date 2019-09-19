# array = [6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49]
array = [7, 15, 36, 39, 40, 41]
# array = [3, 7, 8, 5, 12, 14, 21, 13, 18]
length = len(array)


def find_median(a):
    size = len(a)
    if len(a) % 2 == 0:
        return round((a[size//2 - 1] + a[size//2])/2, 1)
    else:
        return a[size//2]


def quartiles(array):
    array.sort()
    length = len(array)

    if length % 2:  # odd length
        lower_half = array[:length//2]
        upper_half = array[length//2 + 1:]
    else:  # even length
        lower_half = array[:length//2]
        upper_half = array[length//2:]

    Q1 = find_median(lower_half)
    Q2 = find_median(array)
    Q3 = find_median(upper_half)
    return Q1, Q2, Q3


q1, q2, q3 = quartiles(array)
print(int(q1))
print(int(q2))
print(int(q3))
