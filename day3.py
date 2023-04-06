# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import numpy as np

# Define Prime Numbers and Output these numbers
def prime_numbers():
    start = 2 # Prime numbers are alway bigger than 1
    step = 1
    end = 20
    list_number = np.arange(start, end, step, dtype=int).tolist()

    prime_candidates = [2]
    for i in list_number:
        for j in list_number[:list_number.index(i)]:
            if i % j != 0:
                prime_candidates.append(i)

    return prime_candidates


print(prime_numbers())