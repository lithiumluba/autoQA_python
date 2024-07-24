# TO DO: Get value of href attribute for tag a
# Do it:
# using string methods
# using regular expressions

import re
with open('wiki_page.txt') as file:
    content = file.read()

pattern = r'<a href="([^"]+)"'
matches = re.findall(pattern, content)

print(matches)
