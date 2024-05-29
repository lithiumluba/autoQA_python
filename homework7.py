# Output a triangle of user-entered size.
# There are NO spaces at the end of lines.
# DO NOT use methods of string type.

size = int(input("Enter a size of triangle: "))
i = 1
while size >= i:
    print((size-i) * " " + i * '*')
    i += 1
