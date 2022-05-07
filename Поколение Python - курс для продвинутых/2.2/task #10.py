for i in range(int(input())):
    string = input()
    for symbol in "anton.":
        if symbol == ".":
            print(i + 1, end=' ')
            break
        elif symbol in string:
            string = string[string.find(symbol) + 1:]
        else:
            break
