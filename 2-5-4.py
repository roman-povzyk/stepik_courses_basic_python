a = [int(i) for i in input().split()]
b = []

if len(a) == 1:
    print(a[0])
else:
    for i in range(len(a) - 1):
        b.append(a[i-1] + a[i+1])
        if i == len(a) - 2:
            c = a[0]+a[-2]
            b.append(c)

print(' '.join([str(i) for i in b]))

