# The user enters a string. Print True if the string is a palindrome, otherwise False.
# A palindrome is a string that reads the same way from the left and from the right.
# If there are leading or trailing spaces in the line, they should not be taken into account.
# The check must be case-insensitive.
# Solve at least in TWO ways.

user_input = str(input("Enter some letters: "))
clear = user_input.strip().lower()

# FIRST_WAY
# if clear == clear[::-1]:
#     print("True")
# else:
#     print("False")

# SECOND_WAY
clear2 = ""
n = int(len(clear)-1)
while n >= 0:
    clear2 += clear[n]
    n -= 1
if clear == clear2:
    print("True")
else:
    print("False")
