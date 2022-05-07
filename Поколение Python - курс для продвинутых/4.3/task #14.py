def chunked(array):
    lst = [[]]
    index = 0
    for i in range(1, len(array) + 1):
        for j in range(0, len(array) - index):
            lst.append(array[j:j+i])
        index += 1
    return lst

print(chunked(input().split()))
