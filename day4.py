# Day 4 - Large Palindrome Product

"""
Thought Process:
1) Define a Palindrome
> 2 paths: odd and even
1.1: odd palindrome (middle number does not have to be included)
1.2: even palindrome - use of symmetry!
2) Find the largest palindrome made from the product of two 3-digit numbers
"""

import numpy as np


def define_palindrome(num):
    num = num
    reverse = 0

    while num != 0:
        reminder = num % 10
        reverse = (reverse * 10) + reminder
        num = num // 10

    return reverse


# main
three_digit = np.arange(100, 1000, 1).tolist()
factor_list = []
for i in three_digit:
    for j in three_digit:
        factor = i * j
        factor_list.append(factor)

    # three_digit.pop(0)
    # can update this with removal of double calculations

# check for which two 3-digits multiplications are a palindrome
list_palindrome = []
for i in factor_list:
    output = define_palindrome(i)
    if i == output:
        list_palindrome.append(i)

print(max(list_palindrome))





