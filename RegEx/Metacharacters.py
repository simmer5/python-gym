import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gr3y"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")
#======================================
pattern1 = r"^gr.y$"

if re.match(pattern1, "grey"):
   print("Match 1")

if re.match(pattern1, "gray"):
   print("Match 2")

if re.match(pattern1, "stingray"):
   print("Match 3")

#search function matches all strings that contain any one of the characters defined

pattern = r"[aeiou]" 

if re.search(pattern, "grey"):
   print("Match 1")

if re.search(pattern, "qwertyuiop"):
   print("Match 2")

if re.search(pattern, "rhythm myths"):
   print("Match 3")


#matches strings that contain two alphabetic uppercase letters followed by a digit.

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
    print("Match 1")

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "1ab"):
    print("Match 3")

#The pattern [^A-Z] excludes uppercase strings. 
#Note, that the ^ should be inside the brackets to invert the character class.

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
   print("Match 1")

if re.search(pattern, "AbCdEfG123"):
   print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
   print("Match 3")

"""
Some more metacharacters are *, +, ?, { and }.
These specify numbers of repetitions. 
* matches 0 or more occurrences of the preceding expression.
+ matches 1 or more occurrence of the preceding expression.
? means "zero or one repetitions".
 {x,y} means "between x and y repetitions of something".
"""
pattern = r"g+"

if re.match(pattern, "g"):
   print("Match 1")

if re.match(pattern, "gggggggggggggg"):
   print("Match 2")

if re.match(pattern, "abc"):
   print("Match 3")
#======================================

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")
#========================================
pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
   print("Match 1")

if re.match(pattern, "icecream"):
   print("Match 2")

if re.match(pattern, "sausages"):
   print("Match 3")

if re.match(pattern, "ice--ice"):
   print("Match 4")


#=======================================
#"9{1,3}$" matches string that have 1 to 3 nines.
pattern = r"9{1,3}$"

if re.match(pattern, "9"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")

if re.match(pattern, "9999"):
   print("Match 3")