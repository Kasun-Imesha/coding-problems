import re

text = """101 COM    Computers
205 MAT   Mathematics
189 ENG   English"""

regex = re.compile('\s+') #\s-white space, +-one or more

# 1. split the text around 1 or more space characters
print("1. split the text around 1 or more space characters")
# method I
print("method I")
print(re.split('\s+', text))

# method II
print("method II")
print(regex.split(text))

print("2. find all numbers within the text")
text2 = """COM    Computers
205 MAT   Mathematics 189"""
regex_num = re.compile('\d+') #\d-integers, +-one or more, *-none or more
print(regex_num.findall(text2))

print("3. Search and Match")
print("re.search()-returns a particular match object that contains the starting and ending positions of the first occurrence of the pattern")
s = regex_num.search(text2)
print("Method I-start and end positions")
print('Starting Position: ', s.start())
print('Ending Position: ', s.end())
print(text2[s.start():s.end()])

print("Method II-group()")
print(s.group())

print("re.match()-requires the pattern to be present at the beginning of the text")
m = regex_num.match(text2)
print(m)

print("4. Text substitution")
text = """101   COM \t  Computers
205   MAT \t  Mathematics
189   ENG  \t  English"""

print("replace one or more spaces with single space")
regex = re.compile('\s+')
print("Method I")
print(regex.sub(' ', text))

print("Method II")
print(re.sub('\s+', ' ', text))

print("Exclude newline character \\n")
regex = re.compile('((?!\n)\s+)')
print(regex.sub(' ', text))


print("5. Regex groups")
text = """101   COM   Computers
205   MAT   Mathematics
189   ENG    English""" 

print(" extract all course numbers")
print(re.findall('[0-9]+', text)) #[0-9]-numbers from 0-9, +-one or more

print("extract all course codes")
print(re.findall('[A-Z]{3}', text)) #[A-Z]-capital letters, {3}-length is 3

print("extract all course names")
print(re.findall('[A-Za-z]{4,}', text)) #[A-Za-z]-all upper and lowercase letters, {4,}-length is 4 or more

print("extract all groups")
course_pattern = "([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})"
print(re.findall(course_pattern, text))

print("6. Greedy vs Lazy matching")
print("Greedy search")
print("The default behavior of regular expressions is to be greedy. That means it tries to extract as much as possible until it conforms to a pattern even when a smaller part would have been syntactically sufficient.")
text = "< body>Regex Greedy Matching Example < /body>"
print(re.findall('<.*>', text)) #.-one character except new line, *-none or more

print("Lazy search")
print("Lazy matching, on the other hand, ‘takes as little as possible’.")
print(re.findall('<.*?>', text))
