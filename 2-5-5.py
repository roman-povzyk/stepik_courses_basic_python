list_one = input().split(" ")
list_two = []
# print(len(list_one))

for i in range(len(list_one)):
    if list_one.count(list_one[i]) > 1 and list_two.count(list_one[i]) == 0:
        list_two.append(list_one[i])

list_three = sorted(list_two)
print(*list_three)