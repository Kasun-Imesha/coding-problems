import re

# Q) Extract the user id, domain name and suffix from the following email addresses.

emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""

# desired_output = [('zuck26', 'facebook', 'com'),
#  ('page33', 'google', 'com'),
#  ('jeff42', 'amazon', 'com')]

user_id = re.compile("(\w+)@")
domain = re.compile("@(\w+)\.")
suffix = re.compile("\.(\w+)")

all = re.compile("(\w+)@(\w+)\.(\w+)")

print(user_id.findall(emails))
print(domain.findall(emails))
print(suffix.findall(emails))
print(all.findall(emails))


