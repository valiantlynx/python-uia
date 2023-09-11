#variable name = value in variable
num_integer = 4 #integer or whole number
num_float = 4.0 #Float or decimal number
num_string = "4" #String or text
num_list = [4, 4.0, "4"] #List or array filled with int, float and string

a = 4
b = 5

print(a+b)
def add(a,b): #adds a to b
    return a+b

c = add(a, b)

def sub(a,b): #subtracts b from a
    output = a-b
    return output

def mul(a,b):
    return a*b

def div(a, b):
    return a/b

d = a**2 #a squared or a²

from math import sqrt #Importing square root from the library math

def pytagoras(a, b):
    return sqrt(a**2 + b**2)

#Getting the hypothenuse of 2,4
print(pytagoras(2, 4))


#Looping
for e in range(10):
    print(e)#Loops from 0 to 10 and prints (0,1,2,3,4,5,6,7,8,9)

listOfNumbers = [1,2,3,4,5,6,7,8,9,10]

for f in range(len(listOfNumbers)):
    print(listOfNumbers[f])#Prints the first, second, third element and so on
                #prints 1,2,3,4,5,6,7,8,9,10

def loopThroughList(aList):
    for i in range(len(aList)):
        print(aList[i]) #Prints each of the elements in a list

listOfNames = ["John", "Jane", "Smith"]
loopThroughList(listOfNames) #Prints the name

def getEvenNumOnly(aList):
    for a in range(len(aList)-1, -1, -1): #Makes a for loop that goes backwards through the list
        if aList[a] % 2 == 1: #Check if the number is divisible by 2, if you divide it by 2 and get remainder of 1
            del aList[a]#deletes the element
    return aList

def print_num_times_5(aList):
    for a in range(len(aList)):
        print(aList[a]*5)


import random

randomNum = random.randint(9001)

def add_random_num(aList, num):
    for a in range(len(aList)):
        aList[a] += num
    return aList

def div_random_num(aList, num):
    for a in range(len(aList)):
        aList[a] /= num

    return aList

#Python loop
for number in num_list:
    print(number)