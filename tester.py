import requests
linesInFile=["export const testLines = \n[\n"]
ips = ['51.146.52.243', '212.33.205.125']
tmp =''
URL = 'https://ipwhois.app/json/'

for i in ips:
    tmp = URL+i
    print (tmp)
    r = requests.get(url=tmp)
    data = r.json()
    print (data['isp'])
    s = "{from:[%s,%s],to:[-74.012084,40.8042674], stroke:'#FF5533', strokeWidth:1, strokeLinecap:'round'}\n" % (data['longitude'], data['latitude'])
    linesInFile.append(s)
linesInFile.append("]\nexport default {testLines};")

f = open("test.js", 'a')
for i in linesInFile:
    
    f.write(i)
f.close()
