print(sum([1,2,3]))

def custom_sum(list_of_nums):
    total = 0
    for num in list_of_nums:
        total += num
    return total

def custom_product(list_of_nums):
    total = 1
    for num in list_of_nums:
        total *= num
    return total