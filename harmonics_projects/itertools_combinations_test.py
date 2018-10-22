from itertools import combinations

a_list = [3, 3, 2, 5]

n = len(a_list)
m = n

comb_list = []

while m > 0:
    comb_list.append(combinations(a_list, m))
    m -= 1

for sub_list in comb_list:
    for comb in sub_list:
        print(comb)