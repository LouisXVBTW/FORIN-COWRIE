f = open("final.txt", 'r')
u=[]
for i in f:
    print (i)
    u.append(i.replace('\n',''))
count = 0
for i in range(5, len(u)):
    tmp = ''.join(x for x in u[i] if x.isdigit())
    count += int(tmp)
print (count)
