# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings
first_name = "Ana"
food = "greek yoghurt"
email = "anaiscoding@gmail.com"

# Integers
age = 22
quantity = 3
num_of_students = 30

# Float
price = 10.99
gpa = 4.0
distance = 5.5

# Boolean
is_student = True
# is_student = False
for_sale = True
is_online = True

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")
    
if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")
    
if is_online:
    print("You are online")
else:
    print("You are offline")

print(first_name)

#print("first_name")

# f-string

# to use formatted string literals, begin a string with f or F
# before the opening quotation mark or triple quotation mark. Inside
# this string, you can write a Python expression between { and } 
# characters that can refer to variables or literal values.

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km")

print(f"Are you a student?: {is_student}")