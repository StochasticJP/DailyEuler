# find fibonacci sequence up until 4 million and sum up the even-valued numbers

# fibo numbering method
threshold = 4000000
fibo_list = [1, 2]
counter = 0

# working with indexing and shift it up by using a counter
while fibo_list[-1] < threshold:
    new_value = fibo_list[counter] + fibo_list[counter+1]
    fibo_list.append(new_value)
    counter += 1

new_list = fibo_list[0:-1]
even_list = []

# loop through the new list to check which terms are even-valued
for i in new_list:
    if i % 2 == 0:
        even_list.append(i)

print(sum(even_list))
