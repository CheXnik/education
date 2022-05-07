array = input().split()
p, ammount = int(array[0]), 0

for i in array:
    if int(i) > p:
        ammount += 1
    p = int(i)
print(ammount)
