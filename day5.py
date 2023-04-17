import numpy as np
import collections


def check_divisibility():

    # Make a small game where:
    # Create a dict with key-value pairs: Keys(1-20) - Values(bools)
    # These values must all be 1 in the same index for that number to be evenly divisible

    # Create the dict
    keys = range(1, 21)
    num_dicts = {}
    for i in keys:
        num_dicts[i] = []

    # Supply the dict
    nums = range(1, 501)
    for j in nums:
        for key in num_dicts:
            if j % key == 0:
                num_dicts[key].append(1)
            elif j % key != 0:
                num_dicts[key].append(0)

    return num_dicts


# main
dicts_values = check_divisibility()

# obtain the values(lists) of all keys and
# loop through each index and check at which index has a 1
list_val = []
for key in dicts_values: # obtain value lists for each key
    list_val.append(dicts_values[key])


list_idx = []
for number in list_val:
    check_list = [index+1 for (index, item) in enumerate(number) if item == 1]
    for i in check_list:
        list_idx.append(i)

    check_list.clear()

list_idx.sort()  # sort list

counter = collections.Counter(list_idx)  # Dict type output

# Reverse any mapping - whether Counter or Dict
# rev = {v: k for k, v in counter.items()}
key_20 = [key for key, value in counter.items() if value == 10]
print(counter)










