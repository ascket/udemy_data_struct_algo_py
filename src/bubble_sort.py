def bubble_sort1(l):
    count = 1
    while count < len(l):
        for i in range(len(l) - count):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
        count += 1
    return l


def bubble_sort2(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                tmp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = tmp
    return l
