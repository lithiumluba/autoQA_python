# User enters height and width of rectangle (integer numbers), and any symbol.
# Output a rectangle made up of the entered character of a given size.
# There are NO spaces at the end of lines.

height = int(input("Enter a height: "))
width = int(input("Enter width: "))
some_sym = input("Input any symbol: ")
i = 0
while i < height:
    i += 1
    print(width*some_sym)
