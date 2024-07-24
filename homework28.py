# TO DO: Email address validator using regular expressions
# Write function using regular expressions that takes email as string,
# and returns True if the string is a valid address, otherwise False.
# Valid address is considered:
# - '@' comes before '.'
# - the string does not start with '@' and does not end with '.'
# - symbols except '@' and '.' should be letters and decimal digits
# - containing only one '@' and only one '.'

import re


def is_valid_email(email):

    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
    if re.match(pattern, email):
        return True
    else:
        return False


email = "aaa@bbb.ccc"    # True

# Some more tests:
# False -> @lithium.gmail;  lithium@gmail.com. ; lithium.gmail@com; lithium@@com.ua
# True -> lithium@gmail.com; lithium08@gmail1.com

result = is_valid_email(email)
print(result)
