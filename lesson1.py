print('hello world')

#list- indexed array that dont need
list1 = [1, 2, 3, 4]
list1 = [0, 2, 3, 4]

# for i, data in enumerate(list1):
#     print(f'at index: {i}, finnes: {list1[data]}')

def list_of_numbers(some_list: list):
    return sum(some_list)

def combine_sum(some_list1: list, some_list2: list):
    return list_of_numbers(some_list1) + list_of_numbers(some_list2)


print(combine_sum(some_list1=list1, some_list2=list1))