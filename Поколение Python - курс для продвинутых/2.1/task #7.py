num = input()

if int(num) > 999:
    num = [a for a in num]
    num = num[::-1]
    d = 0
    for _ in range(len(num)):
        index = _ + 1
        if index % 3 == 0 and (index + d) != len(num):
            num.insert((index + d), ",")
            d += 1
    print("".join(num[::-1]))
else:
    print(num)