# There's a string with email address.
# Print True if the string is a valid address, otherwise False.
# Valid address is considered:
# - '@' comes before '.'
# - the string does not start with '@' and does not end with '.'
# - symbols except '@' and '.' should be letters and decimal digits
# - containing only one '@' and only one '.'
# Specify strings for testing your code in comments.
# DO NOT use regular expressions.

email_adress = str(input("Input please your email: "))
part1 = email_adress.split("@")
part2 = part1[1].split(".")

if (not (email_adress.startswith('@') and email_adress.endswith('.')) and email_adress.count('@') == 1
        and email_adress.count('.') == 1
        and email_adress.find("@") < email_adress.find('.') and part1[0].isalnum()
        and part2[0].isalnum() and part2[1].isalnum()):
    print("True")
else:
    print("False")

#     False -> @lithium.gmail;  lithium@gmail.com. ; lithium.gmail@com; li$*@gmail.c*m; lithium@@com.ua
#     True -> lithium@gmail.com; lithium08@gmail1.com
