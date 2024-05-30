# The user enters the minimum and maximum width of the diamond pattern.
# Print a "diamond" with given dimensions composed of '*' symbols.
# If the entered minimum width is greater than the maximum width,
# print a warning and terminate the program.
# If the difference between the maximum and minimum widths
# is not a multiple of 2, print a warning and terminate the program.
# There are NO spaces at the end of lines.
# DO NOT use methods of string type


while True:
    user_input1 = input("Enter q if you want to stop.\nEnter minimal width: ")
    if user_input1 == 'q':
        print("Thank you for attending! Bye!")
        break
    else:
        try:
            min_width = int(user_input1)
            max_width = int(input("Enter maximum width: "))

            if min_width > max_width:
                print("Warning! The entered minimum width cannot be greater than the maximum width.")
                exit()
            if ((max_width - min_width) % 2) != 0:
                print("Warning! The difference between the maximum and minimum widths cannot be multiple of 2")
                exit()

            for i in range(min_width, max_width + 1, 2):
                spaces = ' ' * ((max_width - i) // 2)
                if i == min_width:
                    stars = '*' * i
                    print(spaces + stars)
                    continue
                stars = '*' + (i - 2) * " " + '*'
                print(spaces + stars)

            for i in range(max_width - 2, min_width - 1, -2):
                spaces = ' ' * ((max_width - i) // 2)
                if i == min_width:
                    stars = '*' * i
                    print(spaces + stars)
                    continue
                stars = '*' + (i - 2) * " " + '*'
                print(spaces + stars)
        except ValueError:
            print("Entered value can’t be casted in 'int'")

        else:
            print('There is your diamond')
        finally:
            print("---------Another round---------")
