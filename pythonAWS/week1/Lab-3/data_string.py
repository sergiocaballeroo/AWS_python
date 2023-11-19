#Introduction to string data types

myString = "This is a string"

print(myString)
print(type(myString))
print(myString + " is of the data type" +str(type(myString)))

a = '1'
b = "1"
print("Concatenate strings")
print(a+b)

#Getting information from user with "input()" function

name = input("What is your name? ")
print(name)
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))