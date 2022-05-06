raz_array, array =[], input().split()

for i in array:
    if int(i) not in raz_array:
        raz_array.append(int(i))

print(len(raz_array))
