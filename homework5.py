# Output the maximum number of 3 user-entered numbers.
# # DO NOT use built-in functions. Use only flow control instructions (ifs, loops)

lst = []
for i in range(3):
    lst.append(int(input("Enter a number,please: ")))

max_value = lst[0]
for element in lst:
    if max_value < element:
        max_value = element
print("max value is: ", max_value)

