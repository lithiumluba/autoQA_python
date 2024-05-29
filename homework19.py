# There is a list consisting of dictionaries. Each dictionary describes a user and has two keys:
# 'name' (str) and 'age' (int).
# Create and output a list of users' names whose age is 18 years (including) or older.

users = [
    {'name': 'Luarvik L. Luarvik',
     'age': 17},
    {'name': 'Olaf Andvarafors',
     'age': 18},
    {'name': 'Brun Du Barnstokr',
     'age': 19}
]
adult_users = []
for user in users:
    if user['age'] >= 18:
        adult_users += [user['name']]
print("There is a list of adult users:\n", adult_users)
