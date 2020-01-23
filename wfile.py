order={'bread':30,'Jam':20}
file=open("sales.txt",'w')
for items in order:
	file.write(items+'\n')
file.close()


