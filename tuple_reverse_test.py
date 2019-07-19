# Reversing a tuple using slicing technique
# def Reverse(tp):
#     tp1 = tp[::-1]
#     return tp1
# tp = ('z', 'a', 'd', 'f', 'g', 'e', 'e', 'k')
# print(Reverse(tp))


# Reversing a list using reversed()
def Reverse(tuples):
    new_tup = ()
    for k in reversed(tuples):
        new_tup = new_tup + (k, )
    print(new_tup)


# Driver Code
tuples = (10, 11, 12, 13, 14, 15)
Reverse(tuples)