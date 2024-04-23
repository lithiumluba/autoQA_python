# Create list of 3 countries names.
# Create dictionary of 3 key-value pairs.
# Key should be country name from the list and value should be string with its capital.
# Output each pair on separate lines. Separate key from value with colon and space:

countries = ["Ukraine", "Spain", "Italy"]
capital = {countries[0]: 'Kyiv',
           countries[1]: 'Madrid',
           countries[2]: 'Rome'
           }
print(countries[0], capital[countries[0]], sep=': ')
print(countries[1], capital[countries[1]], sep=': ')
print(countries[2], capital[countries[2]], sep=': ')
