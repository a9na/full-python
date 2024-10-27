# Typecasting = the process of converting a variable
#               from one data type to another
#               str(), int(), float(), bool()


name = "Ana Novkovic"
age = 22
gpa = 4.0
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#gpa = int(gpa)

# print(gpa)


# age = float(age)

# print(age)


age = str(age)

#age += 1  - TypeError: can only concatenate str (not "int") to str
age += "1"  # string concatenation

print(age)
print(type(age))

# name = ""  - False
name = bool(name)  # True