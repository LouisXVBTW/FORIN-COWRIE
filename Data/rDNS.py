from dns import resolver,reversename
import time
import glob
startTime = time.time()

def getip():
	tmpIPS = []
	path = "./Data/*ipINFO"
	for filename in glob.glob(path):
			with open(filename, 'r', encoding='utf8') as f:
					for i in f:
						ip = i.replace('\n', '')
						if ip not in tmpIPS:

							tmpIPS.append(ip)

	ipFile = open("/Data/iplist.txt", 'a')
	for i in tmpIPS:
		ipFile.write(i)
		ipFile.write('\n')
	ipFile.close()
	return tmpIPS

def reverseDns(ip):
	dnslist = []
	for i in ip:
		tmp = []
		tmp.append(i)
		try: 
			tmp.append(str(resolver.query(reversename.from_address(ip), 'PTR')[0]))
		except: 
			tmp.append('N/A')
		dnslist.append(tmp)

def main():
	ip = getip()
	dnslist = reverseDns(ip)
	print (dnslist)
	newFile = open("dnslist.txt", 'a')
	for i in dnslist:
		newFile.write(str(i))
		newFile.write('\n')
	newFile.close()
