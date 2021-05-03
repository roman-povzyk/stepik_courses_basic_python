a = int(input())
b = int(input())
c = int(input())

max_arg = max(a, b, c)
min_arg = min(a, b, c)
mid_arg = (a + b + c - min_arg - max_arg)

print(max_arg)
print(min_arg)
print(mid_arg)



#if a > b and a > c:
#    max = a
#elif b > a and b > c:
#    max = b
#elif b > a and b > c:
#    max = b