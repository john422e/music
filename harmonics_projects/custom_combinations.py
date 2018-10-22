from itertools import combinations

def make_all_combinations(iterable):
    m = len(iterable)
    combination_list = []
    while m > 0:
        combination_list.append(combinations(iterable, m))
        m -= 1
    all_combinations = []
    for sub_list in combination_list:
        for combination in sub_list:
            all_combinations.append(combination)
    return all_combinations

def multiply_combinations(combination_list, return_set=False):
    product_list = []
    for combination in combination_list:
        product = 1
        for num in combination:
            product *= num
        product_list.append(product)
    if return_set:
        product_list = sorted(set(product_list))
    return product_list
