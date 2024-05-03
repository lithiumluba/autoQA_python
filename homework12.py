# The program has a line `string`.
# Print the all words, containing the letter 'o' (in any case (upper/lower)) twice, as a title.
string_a = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."
word_list = string_a.title().split()
print(word_list)
result = ""
for word in word_list:
    if word.count("o") == 2:
        result += word + " "
print("Result:", result)
