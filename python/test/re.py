import re

string=r"#include<stdio.h>"
print(string)
com = re.compile(r'\#include<[a-zA_Z\.]+>')
match = com.match(string)
print(match.group())
