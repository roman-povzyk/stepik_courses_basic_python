s2 = 0
a1 = int(input())
s = a1
s2 = a1 * a1

while s != 0:
    a = int(input())
    s += a
    s2 += a * a
    if s == 1:
        break

print(s2)