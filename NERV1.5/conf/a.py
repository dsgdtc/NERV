server_list=[]
with open ("server_list.conf") as f:
	for line in f.readlines():
		print line
		server_list.append(line.split())
print server_list
