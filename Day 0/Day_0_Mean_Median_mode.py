number = 10
array = '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'
array = list(map(int, array.split()))


def find_mean(a):
    return round(sum(a)/number, 1)


def find_median(a):
    a = sorted(a)
    if len(a) % 2 == 0:
        return round((a[number//2 - 1] + a[number//2])/2, 1)
    else:
        return a[number//2]


def find_mode(a):
    a = sorted(a)
    counts = {i: a.count(i) for i in a}
    sorted_x = sorted(counts.items(), key=lambda z: z[1], reverse=True)

    return sorted_x[0][0]


print(find_mean(array))
print(find_median(array))
print(find_mode(array))
