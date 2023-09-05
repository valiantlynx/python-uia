import math 
#write 3 func that processes numbers in some way and returns the list of numbers.
listA = [1,2,3,4,5,6,7,8,9,24,556,23,46,543]

def turn_to_even_no(somelist: list) -> list:
    some_local_list = []
  
    for i, data in enumerate(somelist):
        if ((data % 2) == 1):
            #the number is even
            some_local_list.append(data)
    return some_local_list

def turn_to_odd_no(somelist: list) -> list:
    some_local_list = []
  
    for i, data in enumerate(somelist):
        if ((data % 2) != 1):
            #the number is even
            some_local_list.append(data)
    return some_local_list

def find_square_root(somelist: list) -> list:
    for i, data in enumerate(somelist):
        somelist[i] = math.sqrt(data)
        
    return somelist

def find_sum(somelist: list) -> list:
    return sum(somelist)

print(f"sum: {find_sum(somelist=listA)}")
print(f"odd numbers: {turn_to_odd_no(somelist=listA)}")
print(f"even numbers: {turn_to_even_no(somelist=listA)}")
print(f"square root numbers: {find_square_root(somelist=listA)}")


#write a func that takes the sum of a list and returns the sum which is a float