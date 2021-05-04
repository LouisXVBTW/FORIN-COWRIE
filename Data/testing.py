import ast
n = []


f = open("LDNipINFO", "r", encoding="utf8")
f1 = open("NYCipINFO", 'r', encoding='utf8')
f2 = open("SINGipINFO", 'r', encoding='utf8')
info = ast.literal_eval(f.read())
info1 = ast.literal_eval(f1.read())
info2 = ast.literal_eval(f2.read())



u = info + info1 + info2

f = open('ipdata.txt', 'r')


for i in f:
    i = i.replace('\n', '')
    for line in u:
        if line['ip'] == i:
            n.append(line['country'])
            break
        else:
            pass

end = {i:n.count(i) for i in n}

thing = sorted( ((v,k) for k,v in end.items()), reverse=True)

print (thing)

this = open("final.txt", 'a')
for i in thing:
    this.write(str(i)+'\n')
this.close()
                    
