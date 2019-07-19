import re

s= "hello from radhika@gmail.com to radhika1@yahoo.com about the meeting @2pm"
lst = re.findall('\s+@\s+',s)
print(lst)
