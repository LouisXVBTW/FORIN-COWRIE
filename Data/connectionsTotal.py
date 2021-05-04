import json
import glob

#d = open("ipdata.txt", 'a')

path = './SING/cowrie.json.*'
listOFips=[]
for filename in glob.glob(path):
    with open(filename, 'r') as f:
        for i in f:
            j=json.loads(i)
            try:
                ip = j['src_ip']
                
                listOFips.append(ip)
            except:
                pass
path = './LDN/cowrie.json.*'
for filename in glob.glob(path):
    with open(filename, 'r') as f:
        for i in f:
            j=json.loads(i)
            try:
                ip = j['src_ip']
                
                listOFips.append(ip)
            except:
                pass
path = './NYC/cowrie.json.*'
for filename in glob.glob(path):
    with open(filename, 'r') as f:
        for i in f:
            j=json.loads(i)
            try:
                ip = j['src_ip']
                
                listOFips.append(ip)
            except:
                pass

print (listOFips)
