# There is a two-dimensional list of Latin letters. Sort the letters by columns.
# We assume that the list is rectangular.
# DO NOT use built-in functions map and zip.

sorted_two_dim_lst = []
two_dim_lst = [['a', 'c', 'e'],
               ['f', 'b', 'a'],
               ['a', 'n', 'k'],
               ['e', 'l', 'i']]

num_rows = len(two_dim_lst)
num_column = len(two_dim_lst[0])

sorted_columns = [[] for _ in range(num_column)]

for col in range(0, num_column):
    for row in range(0, num_rows):
        sorted_columns[col].append(two_dim_lst[row][col])

for col in range(num_column):
    sorted_columns[col].sort()

sorted_two_dim_lst = [['' for _ in range(num_column)] for _ in range(num_rows)]

for col in range(num_column):
    for row in range(num_rows):
        sorted_two_dim_lst[row][col] = sorted_columns[col][row]
print('Initial list:\n', two_dim_lst[0], '\n', two_dim_lst[1], '\n', two_dim_lst[2], '\n', two_dim_lst[3], '\n')
print('Result: \n', sorted_two_dim_lst[0], '\n', sorted_two_dim_lst[1], '\n', sorted_two_dim_lst[2], '\n',
      sorted_two_dim_lst[3])
