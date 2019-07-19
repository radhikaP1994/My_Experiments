# Function to reverse a string
def reverse(string):
    string2 = string[0::]
    string = string[::-1]

    print(string)
    print(string2)
    return string


s = "Geeksforgeeks"

print("The original string  is : ")
print(s)

print("The reversed string is : ")
print(reverse(s))
