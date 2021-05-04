from dns import resolver,reversename
import time
import glob
import multiprocessing
startTime = time.time()

def getip():
	aa = []
	inccc = 1066660/5
	incc = 0
	inc = 1066660/5
	for _ in range(0,5):
		bb = multiprocessing.Process(target=multiIP, args=[incc, inc])
		bb.start()
		aa.append(bb)
	for i in aa:
		i.join()
	return tmpIPS

def multiIP():
	tmpIPS = []
	f = open('ipdata.txt', 'r')
	for i in f:
		i = i.replace('\n', '')
		if i not in tmpIPS:
			tmpIPS.append(i)
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
		print (tmp)

def main():
	ip = getip()
	dnslist = reverseDns(ip)
	print (dnslist)
	newFile = open("dnslist.txt", 'a')
	for i in dnslist:
		newFile.write(str(i))
		newFile.write('\n')
	newFile.close()


if __name__ == "__main__":
	aa = multiIP()
	print (aa)
	reverseDns(aa)