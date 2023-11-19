#@author: sergio_caballero


print("Python has tree numeric types: int, float, and complex")

#int data type

print("Creating a variable and storing a int on it:")

myValue=4
print(myValue)

print("To get the data type of the variable we use type() function")


print(type(myValue))

print("To combine text and numbers, we can use the str() function")
print(str(myValue) + " is of the data type " + str(type(myValue)))

print("Variables on python are dinamic")
myValue = 3
print("So the same variable change and now is: " +str(myValue))
#float data type
print("Now working on with float")
floatValue=3.14
print(floatValue)

print(type(floatValue))

print(str(floatValue) +" is of the data type" + str(type(floatValue)))
floatValue2 = 0.0000000000000000000001
print(str(floatValue2) +" is also a float")

#Complex data type
complexValue = 5j
print("Now, complex:")
print(complexValue)
print(type(complexValue))
print(str(complexValue) + " is of the data type " +str(type(complexValue)))

#Boolean

bool=True
print(bool)
print(str(bool) +" is of the data type "+str(type(bool)))