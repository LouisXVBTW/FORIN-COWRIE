import json
import glob
from tabulate import tabulate

#d = open("ipdata.txt", 'a')

path = './SING/cowrie.json.*'
users= []
passs= []
combos= []
for filename in glob.glob(path):
    with open(filename, 'r') as f:
        for i in f:
            j=json.loads(i)
            try:
                foo = j['username']
                bar = j['password']
                this = j['username']+' '+j['password']
                users.append(foo)
                passs.append(bar)
                combos.append(this)
            except:
                pass
path = './LDN/cowrie.json.*'
for filename in glob.glob(path):
    with open(filename, 'r') as f:
        for i in f:
            j=json.loads(i)
            try:
                foo = j['username']
                bar = j['password']
                this = j['username']+' '+j['password']
                users.append(foo)
                passs.append(bar)
                combos.append(this)
            except:
                pass
path = './NYC/cowrie.json.*'
for filename in glob.glob(path):
    with open(filename, 'r') as f:
        for i in f:
            j=json.loads(i)
            try:
                foo = j['username']
                bar = j['password']
                this = j['username']+' '+j['password']
                users.append(foo)
                passs.append(bar)
                combos.append(this)
            except:
                pass



    

print ('u 1')
u = {i:users.count(i) for i in users}
print ('u 2')
us = sorted( ((v,k) for k,v in u.items()), reverse=True)
print ('p 1')
p = {i:passs.count(i) for i in passs}
print ('p 2')
pa = sorted( ((v,k) for k,v in p.items()), reverse=True)
print ('c 1')
c = {i:combos.count(i) for i in combos}
print ('c 2')
co = sorted( ((v,k) for k,v in c.items()), reverse=True)



data=[]
for i in range(0,5):
    tmp=[]
    tmp.append(us[i])
data.append(tmp)
for i in range(0,5):
    tmp=[]
    tmp.append(pa[i])
data.append(tmp)
for i in range(0,5):
    tmp=[]
    tmp.append(co[i])
data.append(tmp)
print (data)

print (tabulate(data, headers=['usernames', 'passwords', 'combos']))

    
