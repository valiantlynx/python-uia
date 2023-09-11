"""
Topics:
- Lists
- Loops
- Functions
"""

"""
# REMEMBER TO PLAY WITH THE CODE,  TRY THINGS OUT, EXPAND, RUN INTO ERRORS, FIX THE ERRORS, AND RUN INTO MORE ERRORS
"""

"""
######################################################################################################################
################################################# A LITTLE DESCRIPTION  ##############################################
######################################################################################################################
"""


# Task 1: Create 3 functions that performs some numeric operation on a list of numbers and returns a list of numbers
# the operations could be to add or subtract etc.
# Task 2: Crate a function that takes the sum of a list and returns a float
# Note: Give your functions relevant names


"""
######################## READ THIS ######################## 
def - this is crucial, it tells python you're defining a function and it should come before the name of the function
that you are defining

return - this is also crucial if you want your function to return anything, else it will only perform something 
(i.e your instructions) and return None

type hinting - as in the number_one: float. This tells the person reading the 
code what types to put in, and what types to expect, the def func() -> float:  means this function returns a float, 
hence the arrow ->, remember to keep track of your types.

If any questions copy paste this into ChatGPT and say explain, or ask me when you see me. 
"""

"""
SOLUTIONS
"""


"""
######################################################################################################################
################################################# DEFINING THE FUNCTIONS #############################################
######################################################################################################################
"""


def this_function_is_called_add_function(number_one: float, number_two: float) -> float:
    return number_one + number_two


def this_function_is_called_subtract_function(number_one: float, number_two: float) -> float:
    return number_one - number_two


def this_function_is_called_squared_function(number: float) -> float:
    return number ** 2


def this_function_is_called_sum_function(a_list: list) -> float:
    return sum(a_list)


def this_function_uses_the_add_function_on_a_list_using_enumerate(a_list: list, a_number_to_add: float) -> list:
    # Remember: enumerate returns a position and the number found at that position
    # Try printing position and number_at_position, can you guess what happens?
    for position, number_at_position in enumerate(a_list):
        a_list[position] = this_function_is_called_add_function(
            number_one=number_at_position,
            number_two=a_number_to_add
        )

    return a_list


def this_function_uses_the_add_function_on_a_list_using_range(a_list: list, a_number_to_add: float) -> list:
    # Remember: enumerate returns a position and the number found at that position
    # Try printing position and number_at_position, can you guess what happens?
    for position in range(len(a_list)):
        a_list[position] = this_function_is_called_add_function(
            number_one=a_list[position],
            number_two=a_number_to_add
        )

    return a_list


def this_function_uses_the_subtract_function_on_a_list_using_enumerate(a_list: list, a_number_to_subtract: float) -> list:
    # Remember: enumerate returns a position and the number found at that position
    # Try printing position and number_at_position, can you guess what happens?
    for position, number_at_position in enumerate(a_list):
        a_list[position] = this_function_is_called_subtract_function(
            number_one=number_at_position,
            number_two=a_number_to_subtract
        )

    return a_list


def this_function_uses_the_subtract_function_on_a_list_using_range(a_list: list, a_number_to_subtract: float) -> list:
    # Remember: enumerate returns a position and the number found at that position
    # Try printing position and number_at_position, can you guess what happens?
    for position in range(len(a_list)):
        a_list[position] = this_function_is_called_subtract_function(
            number_one=a_list[position],
            number_two=a_number_to_subtract
        )

    return a_list


def this_function_uses_the_square_function_on_a_list_using_enumerate(a_list: list) -> list:
    # Remember: enumerate returns a position and the number found at that position
    # Try printing position and number_at_position, can you guess what happens?
    for position, number_at_position in enumerate(a_list):
        a_list[position] = this_function_is_called_squared_function(number=number_at_position)

    return a_list


def this_function_uses_the_square_function_on_a_list_using_range(a_list: list) -> list:
    # Remember: for number in range(your_limit) returns a number between 0 and (your_limit - 1)
    # Try printing position, can you guess what happens?
    for position in range(len(a_list)):
        a_list[position] = this_function_is_called_squared_function(number=a_list[position])

    return a_list


def this_function_uses_the_sum_function_on_a_list(a_list:  list) -> float:
    return this_function_is_called_sum_function(a_list=a_list)


"""
######################################################################################################################
################################################# CALLING THE FUNCTIONS ##############################################
######################################################################################################################
"""

# Do you think the result will change if we loop using for _ in range instead for x, y in enumerate?
# The _, x  and y is just random names, don't let them confuse you!


print(f'The list: {[1, 2, 3, 4]}')
print('\nThe Square Function')
print(this_function_uses_the_square_function_on_a_list_using_range(a_list=[1, 2, 3, 4]))
print(this_function_uses_the_square_function_on_a_list_using_enumerate(a_list=[1, 2, 3, 4]))
print('\nThe Subtract Function')
print(this_function_uses_the_subtract_function_on_a_list_using_range(a_list=[1, 2, 3, 4], a_number_to_subtract=2))
print(this_function_uses_the_subtract_function_on_a_list_using_enumerate(a_list=[1, 2, 3, 4], a_number_to_subtract=2))
print('\nThe Add Function')
print(this_function_uses_the_add_function_on_a_list_using_range(a_list=[1, 2, 3, 4], a_number_to_add=2))
print(this_function_uses_the_add_function_on_a_list_using_enumerate(a_list=[1, 2, 3, 4], a_number_to_add=2))
print('\nThe Sum Function')
print(this_function_uses_the_sum_function_on_a_list(a_list=[1, 2, 3, 4]))


print(f'\n\nCombining The Sum Function With The Add And Subtract Function\nWhy do you think we can do this?\n')
print('\nThe Subtract Function')

print(this_function_uses_the_subtract_function_on_a_list_using_range(
    a_list=[1, 2, 3, 4], a_number_to_subtract=this_function_uses_the_sum_function_on_a_list(a_list=[1, 2, 3, 4])
))
print(this_function_uses_the_subtract_function_on_a_list_using_enumerate(
    a_list=[1, 2, 3, 4], a_number_to_subtract=this_function_uses_the_sum_function_on_a_list(a_list=[1, 2, 3, 4])
))

print('\nThe Add Function')
print(this_function_uses_the_add_function_on_a_list_using_range(
    a_list=[1, 2, 3, 4], a_number_to_add=this_function_uses_the_sum_function_on_a_list(a_list=[1, 2, 3, 4])
))
print(this_function_uses_the_add_function_on_a_list_using_enumerate(
    a_list=[1, 2, 3, 4], a_number_to_add=this_function_uses_the_sum_function_on_a_list(a_list=[1, 2, 3, 4])
))
