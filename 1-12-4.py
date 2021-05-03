form = input()
pi = 3.14

if form == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

elif form == "прямоугольник":
    a = int(input())
    b = int(input())
    s = a * b

elif form == "круг":
    r = int(input())
    s = pi * r ** 2

print(s)


