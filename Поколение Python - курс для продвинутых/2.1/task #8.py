kol = int(input())
step = int(input())
vin = 0

for i in range(1, kol+1):
    vin = (vin + step)%i
    print(vin)
print(vin+1)
