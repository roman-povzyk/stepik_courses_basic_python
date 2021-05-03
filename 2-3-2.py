a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c != d:
    print('\t', c,'\t', d)
else:
    print('\t', c)

for i in range(a, b+1):
    if c != d:
        print(i, '\t',i*c, '\t',i*d)
    else:
        print(i, '\t',i*c)

