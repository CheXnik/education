zip_array, array = [], input().split()

zip_array.append([array[0]])
for i in range(1, len(array)):
    if array[i] != array[i-1]:
        zip_array.append([array[i]])
    else:
        zip_array[-1].append(array[i])
print(zip_array)
