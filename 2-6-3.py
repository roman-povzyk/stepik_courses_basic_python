a = input().split(" ")
b = input()
c = []

if a.count(b) == 0:
    c.append("Отсутствует")
else:
    for i in range(len(a)):
        if a[i] == b:
            c.append(i)

print(*c)