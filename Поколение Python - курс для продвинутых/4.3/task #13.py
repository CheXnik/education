def chunked(array, step):
    lst = []
    for i in range(0, len(array), step):
        lst.append(array[i:i+step])
    return lst

print(chunked(input().split(), int(input())))