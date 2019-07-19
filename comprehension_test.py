lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1]
print(lst)

# x**2 is o/p expression
# range (1, 11) is i/p sequence
# x is variable and
# if x % 2 == 1 is predicate part optional

lst1=[x+1 for x in range(1,10) if x%2==0]
print(lst1)

lst2=[x+1 for x in range(1,10)]
print(lst2)

a = 5
table = [[a, b, a * b] for b in range(1, 11)]
print(table)

print([x.lower() for x in ["A","B","C"]])
print([x.upper() for x in ["av","as2","sfg4"]])


str1="Hai this is python list comprhension : 373"
print(str1)
print([x for x in str1 if x.isdigit()])