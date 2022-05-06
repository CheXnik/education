ammount = int(input())
num = []
for i in range(ammount):
    num.append(input())
pr = int(input())

def proverka(num):
    for i in range(len(num)):
        for k in range(len(num)):
            if i != k and int(num[i]) * int(num[k]) == pr:
                return "ДА"
    return "НЕТ"

if ammount <= 1: print("НЕТ")
else: print(proverka(num))