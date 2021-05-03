a = input()
a_list = a.split(" ")
s = 0

for i in a_list:
    s += int(i)

print(s)