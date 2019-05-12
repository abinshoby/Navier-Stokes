# -*- coding: utf-8 -*-
l=["aaaa'aaaaaa",'aaaaa']
d={}
d['amal']=l

for k in d.keys():
    tt=d[k]
    f=[]
    for sent in tt:
            sent=sent.replace("'","\u2000")
            f.append(sent)
print(f)
