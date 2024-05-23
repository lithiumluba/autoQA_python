# Find the sum and product of the elements of the list greater than the number MIN and less than
# the number MAX (both boundaries inclusive).
# If there are no such elements, print None object for both the sum and the product.

input_lst = []
sum_v = None
prod_v = None

for i in range(9):
    input_lst.append(int(input("Enter a number,please: ")))

min_v = int(input('Enter the MIN value: '))
max_v = int(input('Enter the MAX value: '))

for i in input_lst:
    if min_v <= i <= max_v:
        if sum_v is None:
            sum_v = 0
        if prod_v is None:
            prod_v = 1
        sum_v += i
        prod_v *= i

print('lst = ', input_lst)
print('MIN = ', min_v)
print('MAX = ', max_v)
print('.............................')
print('sum = ', sum_v, ', product = ', prod_v)
