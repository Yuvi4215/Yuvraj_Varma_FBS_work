import re

string="""Tester testing software is like new born driving farrari.
Tester can never become developer.
it will take atleast 5+ year to become developer."""

#\w - alphanumeric and underscore
result= re.findall(r"\w",string)

#\W - everything except -alphanumeric and underscore
result= re.findall(r"\W",string)

#\d - digit
result= re.findall(r"\d",string)

#\D - Eveything except- digit
result= re.findall(r"\D",string)

#\s - space, \n, \t etc.
result= re.findall(r"\s",string)

#\S - Eveything except- space, \n, \t
result= re.findall(r"\S",string)

#{digit} -digit no. of characters
result= re.findall(r"\w{3}",string)

#+ - 1 or more occurances
result= re.findall(r"\w+",string)

#\* - 0 or more occurances
result= re.findall(r"\w*",string)

#? - 0 or 1
result= re.findall(r"\w?",string)

#[abc] - a or b or c(any char present inside list[char])
result= re.findall(r"[abc]",string)

#a|b - a or b (any char present "char1 | char2")
result= re.findall(r"a|b",string)

#^ - starting
result= re.findall(r"^\w+",string)

#$ - ending
result= re.findall(r"\W+$",string)

#re.M - Multiline checking
result= re.findall(r"\w",string, re.M)

#re.I - IgnoreCase
result= re.findall(r"tester",string, re.I)
result= re.findall(r"tester",string, re.I|re.M)


print(result)