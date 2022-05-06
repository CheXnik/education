def game(timur, ruslan):
    if timur == ruslan:
        print("ничья")
    elif (timur == "камень" and ruslan != "бумага") or \
        (timur == "бумага" and ruslan != "ножницы") or \
        (timur == "ножницы" and ruslan != "камень"):
            print("Тимур")
    else:
        print("Руслан")

game(input(), input())
