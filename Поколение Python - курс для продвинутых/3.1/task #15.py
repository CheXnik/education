# def func(num1, num2):
#     if num1 % num2 == 0:
#         print("делится")
#     else:
#         print("не делится")
#
# func(int(input()), int(input()))

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']

list1[2][1][2].extend(sub_list)

print(list1)
