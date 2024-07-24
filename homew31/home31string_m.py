# TO DO: Get value of href attribute for tag a
# Do it:
# using string methods
# using regular expressions

# using string methods
hrefs = []
start_index = 0

with open('wiki_page.txt') as file:
    content = file.read()
while True:
    start_index = content.find('<a href="', start_index)
    if start_index == -1:
        break
    start_index += 9
    end_index = content.find('"', start_index)
    href = content[start_index:end_index]
    hrefs.append(href)
    start_index = end_index + 1

print(hrefs)
