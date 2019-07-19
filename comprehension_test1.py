# list_of_squares = []
# for int in range(1, 10):
#     square = int ** 2
#     list_of_squares.append(square)
#
# print(list_of_squares)

ls=[x**2 for x in range(1,10)]
print('List of squares using list comprehension: {}'.format(ls))
# print(ls)
