import json
import glob
import multiprocessing


#d = open("ipdata.txt", 'a')
def main():
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

	return users, passs, combos

	
def one(users):
	print ('u 1')
	u = {i:users.count(i) for i in users}
	print ('u 2')
	us = sorted( ((v,k) for k,v in u.items()), reverse=True)
	f = open('listOFusers.txt', "a")
	print (us)
	for i in us:
		f.write(str(i))
		f.write("\n")
	f.close()

def two(passs):
	print ('p 1')
	p = {i:passs.count(i) for i in passs}
	print ('p 2')
	pa = sorted( ((v,k) for k,v in p.items()), reverse=True)
	f = open('listOFpasswords.txt', "a")
	print (pa)
	for i in pa:
		f.write(str(i))
		f.write("\n")
	f.close()

def three(combos):
	print ('c 1')
	c = {i:combos.count(i) for i in combos}
	print ('c 2')
	co = sorted( ((v,k) for k,v in c.items()), reverse=True)
	f = open('listOFcombos.txt', "a")
	print (co)
	for i in co:
		f.write(str(i))
		f.write("\n")
	f.close()

if __name__ == "__main__":

	users, passs, combos = main()
	aa = multiprocessing.Process(target=one, args=[users])
	bb = multiprocessing.Process(target=two, args=[passs])
	cc = multiprocessing.Process(target=three, args=[combos])

	aa.start()
	bb.start()
	cc.start()

	aa.join()
	bb.join()
	cc.join()






	
