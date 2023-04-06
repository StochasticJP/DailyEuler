# Multiple of 3 or 5

# Find the multiple of 3 and 5 below 1000
number = 1000
three = [0]
five = [0]
counter_three = 0
counter_five = 0
total = 0

list_equals = []
list_not_equals = []

while counter_three < number:
    while counter_five < number:
        new_five = five[-1] + 5
        counter_five += 5
        if new_five < number:
            five.append(new_five)

    new = three[-1] + 3
    counter_three += 3
    if new < number:
        three.append(new)

for equal_number in three:
    if equal_number in five:
        list_equals.append(equal_number)
    else:
        list_not_equals.append(equal_number)

for second_iter in five:
    if second_iter not in three:
        list_not_equals.append(second_iter)


print(sum(list_not_equals) + sum(list_equals))

