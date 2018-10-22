import math

# get max harmonic value
starting_harmonic = int(input("Starting harmonic (4, 8, 16, or 32): "))
# declare list name for groups of interval diads and their combination tones
groups = []

# yields lists for every diad combination from 1 - max val (starting_harmonic)
for harm in reversed(range(1, starting_harmonic)):
    #sum = str(starting_harmonic + harm)
    #sub = str(starting_harmonic - harm)
    group = [starting_harmonic, harm]
    groups.append(group)

print(groups)

big_groups = []

for one, two in groups:
    diad_group = []
    if one == 4:
        loop = 3
    elif one == 8:
        loop = 4
    elif one == 16:
        loop = 5
    elif one == 32:
        loop = 6
    for i in range(loop):
        print(one, two)
        diad = (one, two)
        diad_group.append(diad)
        one = one // 2
    big_groups.append(diad_group)

print(big_groups)

# now get combination tones

# ??? create numpy array — each element in groups should be one row, then each column will divide

def is_prime(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    return prime

def prime_factors(number):
    factors = []
    primes = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    for f in factors:
        prime = True
        if f == 1:
            prime = False
        elif f == 2 or f == 3:
            prime = True
        else:
            for i in range(2, f):
                if f % i == 0:
                    prime = False
                    break
        if prime == True:
            primes.append(f)
    return primes
"""
for group in groups:
    primes = []
    for num in group:
        primes.append(prime_factors(num))
    print(primes)
"""