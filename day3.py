# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import numpy as np

# Define Prime Numbers and Output these numbers

# Check ONLY divisibility by itself and remainder = 0
# Above is always the case usually, so check:
# If there are other divisibility with 0 other than its self then reject number

def prime_numbers():
    start = 2 # Prime numbers are always bigger than 1
    step = 1
    end = 100000 + step
    list_number = np.arange(start, end, step, dtype=int).tolist()

    prime_candidates = []

    for i in list_number:
        store_i = []
        for j in list_number[:list_number.index(i)]:
            if i % j != 0:
                # only get one 'i' at the end of the for loop
                store_i.append(i)

        if len(store_i) == len(list_number[:list_number.index(i)]):
            prime_candidates.append(i)  # add current i to prime candidates

        store_i.clear()  # clear the list to go to the next iteration

    return prime_candidates


# Main - Check largest prime factor of the number 600851475143
# get prime numbers
number = 600851475143
chosen_numbers = prime_numbers()

chosen_primef = []
for i in chosen_numbers:
    if number % i == 0:
        chosen_primef.append(i)

print(max(chosen_primef))
