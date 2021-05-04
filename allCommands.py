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
                ip = j['input']
                
                listOFips.append(ip)
            except:
                pass
path = './LDN/cowrie.json.*'
for filename in glob.glob(path):
    with open(filename, 'r') as f:
        for i in f:
            j=json.loads(i)
            try:
                ip = j['input']
                
                listOFips.append(ip)
            except:
                pass
path = './NYC/cowrie.json.*'
for filename in glob.glob(path):
    with open(filename, 'r') as f:
        for i in f:
            j=json.loads(i)
            try:
                ip = j['input']
                
                listOFips.append(ip)
            except:
                pass

end = {i:listOFips.count(i) for i in listOFips}

thing = sorted( ((v,k) for k,v in end.items()), reverse=True)
for i in range(0,50):
    print (thing[i])
