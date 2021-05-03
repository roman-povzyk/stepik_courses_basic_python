genom = input().upper()
gc = 0

for i in genom:
    if (i == "G") or (i == "C"):
        gc += 1

print(gc/len(genom)*100)
