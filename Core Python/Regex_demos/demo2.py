import re

string="""Tester testing software is like new born driving farrari.
Tester can never become developer.
it will take atleast 5+ year to become developer."""

pattern=re.compile(r"Tester")
result=re.findall(pattern,string)

print(result)