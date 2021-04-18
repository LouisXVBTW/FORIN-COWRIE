import json
import glob
import requests

def main():
    print ("edit me")

    
def addNYC():
    f = open("NYCipINFO.json", "a")
    lineBYline=[]
    tmpIPS=[]
    path = "./NYC/cowrie.json.*"
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            for i in f:
                j=json.loads(i)
                try:
                    ip = j['src_ip']
                    if ip not in tmpIPS:
                        tmpIPS.append(ip)
                    else:
                        pass
                except:
                    pass
    print (tmpIPS)
    
    
    tmp =''
    URL = 'https://ipwhois.app/json/'

    for i in tmpIPS:
        tmp = URL+i
        print (tmp)
        r = requests.get(url=tmp)
        data = r.json()
        lineBYline.append(data)
    print (lineBYline)
    for i in lineBYline:
        f.write("\n")
        f.write(i)
    f.close()
    
    


def addLDN():
    f = open("LDNipINFO.json", "a")
    lineBYline=[]
    tmpIPS=[]
    path = "./LDN/cowrie.json.*"
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            for i in f:
                j=json.loads(i)
                try:
                    ip = j['src_ip']
                    if ip not in tmpIPS:
                        tmpIPS.append(ip)
                    else:
                        pass
                except:
                    pass
    print (tmpIPS)
    
    
    
##    s = ''
##    for i in tmpIPS:
##        s += i + ' '
##    print (s)
    tmp =''
    URL = 'https://ipwhois.app/json/'

    for i in tmpIPS:
        tmp = URL+i
        print (tmp)
        r = requests.get(url=tmp)
        data = r.json()
        lineBYline.append(data)
    print (lineBYline)
    text = str(lineBYline)
    f.write(text)
    f.close()


def addSING():
    f = open("SINGipINFO.json", "a")
    lineBYline=[]
    tmpIPS=[]
    path = "./SING/cowrie.json.*"
    for filename in glob.glob(path):
        with open(filename, 'r') as f:
            for i in f:
                j=json.loads(i)
                try:
                    ip = j['src_ip']
                    if ip not in tmpIPS:
                        tmpIPS.append(ip)
                    else:
                        pass
                except:
                    pass
    print (tmpIPS)
    
    
    
##    s = ''
##    for i in tmpIPS:
##        s += i + ' '
##    print (s)
    tmp =''
    URL = 'https://ipwhois.app/json/'

    for i in tmpIPS:
        tmp = URL+i
        print (tmp)
        r = requests.get(url=tmp)
        data = r.json()
        lineBYline.append(data)
    print (lineBYline)
    text = str(lineBYline)
    f.write(text)
        
def creds(f,t):
    u=[]
    p=[]
    if t == "a":
        for i in f:
            j = json.loads(i)
            try:
                print (j["timestamp"]+"\tSuccessful connection from: "+j['src_ip']+"\n"+j['username']+" --- "+j['password'])
            except:
                pass
    if t == "s":
        for i in f:
            j = json.loads(i)
            try:
                if j['eventid'] == "cowrie.login.success":
                    print (j["timestamp"]+"\tSuccessful connection from: "+j['src_ip']+"\n"+j['username']+" --- "+j['password'])
            except:
                pass
def inputs(f):
    tmp = []
    for i in f:
        j = json.loads(i)
        try:
            
            print ("From: "+j['src_ip']+"\nInput: "+j['input'])
        except:
            pass
    return tmp

if __name__ == "__main__":
    main()
