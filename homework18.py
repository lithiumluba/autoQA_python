# There are lists of testers (names or ids) who:
# - can write test designs
# - can write test scripts
# - can review scripts
# - out of work today (here could be only testers from 3 previous groups)
# Any tester can be listed in one or more groups.
# Create the following sorted lists:
# - all testers in the team
# - testers who can only write scripts
# - testers who are at work today
# - testers who could write and review scripts, and are at work today
# The results should be sorted.

test_design_writers = [1, 3, 5]
test_scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

all_testers = sorted(set(test_design_writers) | set(test_scripters) | set(reviewers))
only_scripters = sorted(set(test_scripters) - set(test_design_writers) - set(reviewers))
at_work_today = sorted(set(all_testers) - set(out_of_office_today))
write_and_review_at_work = sorted(set(test_scripters) & set(reviewers) - set(out_of_office_today))

print("All testers in the team:\n", all_testers)
print("Testers who can only write scripts:\n", only_scripters)
print("Testers who are at work today:\n", at_work_today)
print("Testers who could write and review scripts, and are at work today:\n", write_and_review_at_work)
