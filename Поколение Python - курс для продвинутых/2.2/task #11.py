abv = [chr(i) for i in range(1072, 1104)]
word = input() + " запретил букву"

for symbol in abv:
    if symbol in word:
        print(word, symbol)
        word = " ".join(word.replace(symbol, "").lstrip().split())
