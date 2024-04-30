# Given the entered number n, derive a pattern from numbers
# n could be in range 1 <= n <= 9.
# There are NO spaces at the end of lines.
# DO NOT use methods of string type.
# You could solve this task for n > 9, but it would be task with * :)

n = int(input("Enter the integer number from 1 to 9: "))
if n < 1 or n > 9:
    print("The value that you entered is out of range")
    exit()
k = ""
for j in range(n):
    k = ""
    spaces = ' ' * (n-1-j)
    for i in range(1, j + 2):
        k += str(i)
    for i in range(j, 0, -1):
        k += str(i)

    print(spaces + k)
