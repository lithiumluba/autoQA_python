# TO DO: Time schedule:
# Classes are held on Mondays and Thursdays at 19:15
# The first lesson took place on April 11, 2024.
# Print a list of all classes in the format below (number of lecture are aligned to the right):

from datetime import datetime, timedelta
start_date = datetime(2024, 4, 11, 19, 15)
lectures = []
num_lectures = 32
current_date = start_date

for i in range(1, num_lectures + 1):
    lectures.append(f"Lecture {i:2}: {current_date.strftime('%d %b %Y %H:%M')}")

    if current_date.weekday() == 0:
        days_to_add = 3
    else:
        days_to_add = 4

    current_date += timedelta(days=days_to_add)

for lecture in lectures:
    print(lecture)
