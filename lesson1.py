print('hello world')

#list- indexed array that dont need
list1 = [1, 2, 3, 4, 'A', "@"]
list2 = [0, 2, 3, 4]

for i, data in enumerate(list1):
    #print(f'at index: {i}, finnes: {data}')
    pass

def list_of_numbers(some_list: list):
    return sum(some_list)

def combine_sum(some_list1: list, some_list2: list):
    return list_of_numbers(some_list1) + list_of_numbers(some_list2)


print(combine_sum(some_list1=list2, some_list2=list2))