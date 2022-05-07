import math

def triangle(n):
    array = []
    for i in range(n + 1):
        array.append(int((math.factorial(n)) / (math.factorial(i) * math.factorial(n - i))))
    print(*array)

for i in range(int(input())):
    triangle(i)
