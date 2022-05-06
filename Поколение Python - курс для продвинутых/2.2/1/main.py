points = int(input())
coords = []
for i in range(points):
    coords.append(input().split())

I = 0
II = 0
III = 0
IV = 0

for coord in coords:
    if int(coord[0]) != 0 and int(coord[1]) != 0:
        if int(coord[0]) > 0 and int(coord[1]) > 0: I += 1
        elif int(coord[0]) < 0 and int(coord[1]) > 0: II += 1
        elif int(coord[0]) < 0 and int(coord[1]) < 0: III += 1
        elif int(coord[0]) > 0 and int(coord[1]) < 0: IV += 1

print("Первая четверть:", I)
print("Вторая четверть:", II)
print("Третья четверть:", III)
print("Четвертая четверть:", IV)
