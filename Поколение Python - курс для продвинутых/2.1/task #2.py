massa = float(input())
rost = float(input())

imt = massa/rost**2

if imt < 18.5:
    print("Недостаточная масса")
elif imt <= 25:
    print("Оптимальная масса")
else:
    print("Избыточная масса")
