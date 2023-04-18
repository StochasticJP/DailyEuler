# day 6 - sum square difference
import numpy as np


def sum_of_squares(list):
    list_squared = []
    for i in list:
        square = i**2
        list_squared.append(square)

    number_sum = sum(list_squared)

    return number_sum


def square_of_sum(list):
    sum_list = sum(list)

    number_square = sum_list**2

    return number_square


# main
hundred_nums = np.arange(1, 101, 1).tolist()

# sum of squares
sum_squares = sum_of_squares(hundred_nums)

square_sum = square_of_sum(hundred_nums)

print(square_sum - sum_squares)



