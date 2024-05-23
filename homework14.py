# There is a list consisting of integer numbers.
# Create three lists:
# - to the first list add numbers that are only divisible by 3, but not divisible by 5
# - to the second list add numbers that are divisible by 5, but not divisible by 3
# - to the third list add numbers that are divisible by both 3 and 5

input_lst = []
div3 = []
div5 = []
div3and5 = []

for i in range(16):
    input_lst.append(int(input("Enter a number,please: ")))

print(input_lst, '# Input list')

for item in input_lst:
    if item % 3 == 0 and item % 5 == 0:
        div3and5.append(item)
        continue
    if item % 3 == 0:
        div3.append(item)
        continue
    if item % 5 == 0:
        div5.append(item)
        continue

print(div3, ' # elements divided by 3')
print(div5, ' # elements divided by 5')
print(div3and5, ' # elements divided by 3 and by 5')