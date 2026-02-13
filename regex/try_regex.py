import re

text = """101 COM    Computers
205 MAT   Mathematics
189 ENG   English. Coool"""

text2 = """COM    Computers
205 MAT   Mathematics 189"""

# code = "((?!\n)\s+)"  #whitespace except new line
# code = "\b" # Word boundary
# code = "\." # period
# code = "\w" # any character (including digits)
# code = "\d" # any  digit
# code = "\D" # non digit
# code = "\d+" # one or more digits
# code = "\D+" # one or more non digits
# code = "." # one character except new line
# code = "$" #end of string 
# code = "^" #start of string 
# code = "er|ic" #match er or ic
# code = "[b-e]" #one character from b to e
# code = "[b-e]+" #one or more character from b to e
# code = "[^b-e]" #one character except from b to e
# code = "[^aeiou]" #one character except a, e, i, o, u
# code = "[aeiou]" #one character from a, e, i, o, u
# code = "(Mat)" #Items within parenthesis are retrieved
# code = "(M(at))" #Items within the sub-parenthesis are retrieved
# code = "[ic]{1,}" #One or more continuous occurrences of i or c
# code = "[ic]+" #One or more continuous occurrences of i or c
# code = "[ic]*" #Zero or more continuous occurrences of i or c
# code = "[ic]?" #Zero or one continuous occurrences of i or c
# code = r"Co*l"
# code = r"C+oool"
# code = r"[MATmat]{3}" #match 3 continuous occurances of M, A, T, m, a, t
# code = r"\b[MATmat]{3}\b" #match 3 continuous occurances of M, A, T, m, a, t with boundary on both sides

# code =  r' (\d{1,3}),? '
# code = r'Age[\:\s](\d{1,3})'
code = r'\((\d{1,3})\)'

# code = r".*?(\d{1,3}).*?"
code = r".*?(\d{1,3})\s*[mon]+"
code = r".*?(\d{1,3})\s*[year]+"

regex = re.compile(code)

# text = "Age 26"
# text = "Age:(26)"
text = " 26, "
text = "\n26"
text = "~26\n"
# text = "26"
# text = "i am 26"
# text = "my age is 26"
# text = "26 is m,y age"
text = "i am 26 years and 4 months old"

print(regex.split(text))

print(regex.findall(text))


exit(0)
s = regex.search(text2)
print('Starting Position: ', s.start())
print('Ending Position: ', s.end())
print(text2[s.start():s.end()])

print("Method II-group()")
print(s.group())
