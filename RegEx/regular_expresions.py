import re

"""
The function re.finditer does the same thing as re.findall, 
except it returns an iterator, rather than a list. 

"""

pattern = r"sa"
match = re.search(pattern, "eggspamsausagespam")

if re.match(pattern, "eggspamsausagespam"):
	print("Match")
else:
   print("No match")

if re.search(pattern, "eggspamsausagespam"):
	print("Match search")
	print(match.group())
	print(match.start())
	print(match.end())
	print(match.span())

else:
   print("No match search")
   
print(re.findall(pattern, "eggspamsausagespamsa"))

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)