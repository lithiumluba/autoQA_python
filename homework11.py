# The program has a string `sentences`.
# The string consists of sentences.
# A 'sentence' is a set of characters delimited by periods(. or ...) or the beginning of a line and a period.
# Return list with number of words in each sentence.
# A 'word' is a set of characters between two spaces or the beginning of a line and a space.
# DO NOT use regular expressions.
sentences = "Hello all. Here's pretty cold and hot. Choose yourself."
sentence = sentences.split(". ")
words = ""
words_number = []
for i in sentence:
    words = i.split()
    words_number.append(len(words))
print(sentence)
print(words_number)
