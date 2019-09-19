_ = 6
X = '6 12 8 10 20 16'
F = '5 4 3 2 1 5'

X = list(map(int, X.split()))
F = list(map(int, F.split()))

S = []

for i, j in zip(X, F):
    while j > 0:
        S.append(i)
        j -= 1


def find_median(a):
    size = len(a)
    if size % 2 == 0:
        return round((a[size//2 - 1] + a[size//2])/2, 1)
    else:
        return a[size//2]


def interQuartileRange(array):
    array.sort()
    length = len(array)

    if length % 2:  # odd length
        lower_half = array[:length//2]
        upper_half = array[length//2 + 1:]
    else:  # even length
        lower_half = array[:length//2]
        upper_half = array[length//2:]

    Q1 = find_median(lower_half)
    # Q2 = find_median(array)
    Q3 = find_median(upper_half)
    return Q3 - Q1


print(interQuartileRange(S))
