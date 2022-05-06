array = input().split()
array.insert(0, array[len(array)-1])
print(*array[:-1])
