import math

friends = 10

# friends = friends + 1
# friends += 1

# friends = friends - 2
# friends -= 2

# friends = friends * 3
# friends *= 3

# friends = friends / 2
# friends /= 2

# exponents: 
# friends = friends ** 2
# friends **= 2

# modulus (remainder of any division): 
# remainder = friends % 3
# print (remainder)

print(friends)



# MATH RELATED FUNCTIONS:

x = 3.14
y = 4 
z = 5

# result = round(x)
# result = abs(y)
# result = pow(y, 3)
# result = max(x, y, z)  maximum value of various values
# result = min(x, y, z)

# print(result)



# useful constants and functions

x = 9.9

print(math.pi)
print(math.e)  # exponential constant

# result = math.sqrt(x)
# result = math.ceil(x)
# print (math.trunc(3.5)) # work as floor

result = math.floor(x)

print(result)




# EXERCISES :


# Calculate the circumference of a circle:

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")



# Calculate the area of a circle

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm^2")



# Find the hypothenuse of a right triangle

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt((pow(a, 2) + pow(b, 2)))

print(f"Side C = {c}")