import os
a="F:\python\chapter 2"
b="123.py"
c=os.path.join(a,b)
x="F:\python\chapter 2"
y="Practice.py"
char=os.path.join(x,y)
os.rename(c,char)