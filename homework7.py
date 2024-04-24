# Output a triangle of user-entered size.
# There are NO spaces at the end of lines.
# DO NOT use methods of string type.

size = int(input("Enter a size of triangle: "))
i = 0
while size > i:
    i += 1
    print((size-i)*" ", i * '*')
