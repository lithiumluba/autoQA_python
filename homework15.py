# Find the sum and product of the elements of the list greater than the number MIN and less than
# the number MAX (both boundaries inclusive).
# If there are no such elements, print None object for both the sum and the product.

input_lst = []
sum_v = 0
prod_v = 1
for i in range(8):
    input_lst.append(int(input("Enter a number,please: ")))

max_v = int(input('Enter the MAX value: '))
min_v = int(input('Enter the MIN value: '))

for i in input_lst:
    if min_v <= i <= max_v:
        sum_v += i
        prod_v *= i
    else:
        sum_v = None
        prod_v = None

print('lst = ', input_lst)
print('MIN = ', min_v)
print('MAX = ', max_v)
print('.............................')
print('sum = ', sum_v, ', product = ', prod_v)
