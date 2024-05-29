# There is a text file. Print the longest line in file.
# If there's several lines of maximum length, print the last one.
# Do not use built-in max, sorted functions and file read/readlines method.
max_len = 0
longest_line = ""
my_file = open('homew20.md')
for line in my_file:
    current_len = len(line)
    if current_len >= max_len:
        max_len = current_len
        longest_line = line
my_file.close()
print('The longest line in the file is: ', longest_line)
