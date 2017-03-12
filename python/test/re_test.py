import re
import sys

line = '[132:234:234 234] [adfasg.c-124] [132:234:234 434] [adfasg.c-124] asdfasdf fsd sdf af asd f'
a = re.compile('\[(\d*):(\d*):(\d*) (\d*)\] \[(\D*-\d*)\](.*)')
match=a.match(line)
(h,m,s,ms,file,data)= match.groups()
print(h)

print(m)

print(s)

print(ms)

print(file)

print(data)

