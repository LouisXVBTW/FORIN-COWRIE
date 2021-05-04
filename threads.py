import json
import glob
from threading import Thread


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



    
def one():
	print ('u 1')
	u = {i:users.count(i) for i in users}
	print ('u 2')
	us = sorted( ((v,k) for k,v in u.items()), reverse=True)
	for i in range(0,5):
		print (us[i])

def two():
	print ('p 1')
	p = {i:passs.count(i) for i in passs}
	print ('p 2')
	pa = sorted( ((v,k) for k,v in p.items()), reverse=True)
	for i in range(0,5):
		print (pa[i])

def three():
	print ('c 1')
	c = {i:combos.count(i) for i in combos}
	print ('c 2')
	co = sorted( ((v,k) for k,v in c.items()), reverse=True)
		
	for i in range(0,5):
		print (co[i])


aa = Thread(target = one).start()
bb = Thread(target = two).start()
cc = Thread(target = three).start()




    
