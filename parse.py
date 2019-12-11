def parse():
	file = open('file1.txt','r')
	file2 = open('file2.txt','w+')
	data=file.read()
	data.replace(']','[')
	ll=data.split('[')
	
	for i in ll:
		file2.write(i+'\n')
	file.close()
	file2.close()

if __name__=='__main__':
	parse()