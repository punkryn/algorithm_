import re

S = input()
P = input()

tmp = re.compile(P)
if(tmp.search(S)):
    print(1)
else:
    print(0)