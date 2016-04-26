import os,sys,commands,time
status, result = commands.getstatusoutput("/root/script/NERV/test/expect_password 10.6.114.1 WCGrTP7MUU111 ls") 
print status,result
#if "root@10.6.114.1's password:" in result:
#	print "Error"
