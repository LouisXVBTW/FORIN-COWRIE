import os
import glob
import ast

cityCount =[]
countryCount = []
ispCount = []


f = open("LDNipINFO", "r", encoding="utf8")
f1 = open("NYCipINFO", 'r', encoding='utf8')
f2 = open("SINGipINFO", 'r', encoding='utf8')
info = ast.literal_eval(f.read())
info1 = ast.literal_eval(f1.read())
info2 = ast.literal_eval(f2.read())
for i in info:
    cityN = i['city']
    
    countryN = i['country']
    ispN = i['isp']

    cityCount.append(cityN)
    countryCount.append(countryN)
    if ispN != None:
        ispCount.append(ispN)
for i in info1:
    cityN = i['city']
    
    countryN = i['country']
    ispN = i['isp']

    cityCount.append(cityN)
    countryCount.append(countryN)
    if ispN != None:
        ispCount.append(ispN)
for i in info2:
    cityN = i['city']
    
    countryN = i['country']
    ispN = i['isp']

    cityCount.append(cityN)
    countryCount.append(countryN)
    if ispN != None:
        ispCount.append(ispN)
    

ci = {i:cityCount.count(i) for i in cityCount}

thing = sorted( ((v,k) for k,v in ci.items()), reverse=True)

co = {i:countryCount.count(i) for i in countryCount}

thing2 = sorted( ((v,k) for k,v in co.items()), reverse=True)

ip = {i:ispCount.count(i) for i in ispCount}
thing3 = sorted( ((v,k) for k,v in ip.items()), reverse=True)





count = 0
count1 = 0
count2 = 0
print ("Top 5 city\t\tTop 5 country")
for i in range(0, 5):
    print (str(thing[i])+"\t"+str(thing2[i]))

for i in range(5,len(thing)):
    count += thing[i][0]

for i in range(5,len(thing2)):
    count1 += thing2[i][0]

print ("Other: "+str(count)+"\t\tOther: "+str(count1))

print ("\nTop 10 ISPs used")
for i in range(0,10):
    print (thing3[i])
for i in range(10,len(thing3)):
    count2 += thing3[i][0]
print("Other: "+str(count2))
input("\nPress Enter to exit")

