# There is a list of at least two float elements.
# Create a new list. It should contain elements of
# initial list, and between them should be added average of that elements.

input_lst = []
new_lst = []

for i in range(5):
    input_lst.append(float(input("Enter a number,please: ")))
print("lst = ", input_lst)

new_lst.append(input_lst[0])
for i in range(1, len(input_lst)):
        average = (input_lst[i-1] + input_lst[i]) / 2
        new_lst.append(average)
        new_lst.append(input_lst[i])

print("result: ", new_lst)
