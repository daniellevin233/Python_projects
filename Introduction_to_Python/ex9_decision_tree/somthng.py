def sort(a):
    sorted(a)
    if len(a) == 1:
        return a
    mid = len(a)//2
    b = a[:mid]
    c = a[mid:]
    sort(b)
    sort(c)
    merge(b, c, a)

def merge(b, c, a):
    i, j, k = 0, 0, 0
    while k < len(a):
        if i < len(b) and (j >= len(c) or b[i] < c[j]):
            a[k] = b[i]
            k += 1
            i += 1
        else:
            a[k] = c[j]
            k += 1
            j += 1
    return a
x = [55, 15, 23, 11, 30, 27, 40, 10]
sort(x)

zoo = [[1]*2]*2
zoo[1][0] += 1
print(zoo)  # ?????????????????????????????????????????????????????
lst = [0, 0, 0, 0, 0, 5]
print(list(map(lambda x: x**2, lst)))





