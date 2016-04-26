# *** coding:utf*8 ***
import os,sys,commands,time
import init
import base64
import mydecode
WORKDIR = init.WORKDIR 
result_dict = {}
def traffic_file(add1,add2,ip,passwd,method):
	if method == 'publickey':
		status, result = commands.getstatusoutput("%s/include/expect/traffic_publickey %s root@%s:%s %s" % (WORKDIR,add1,ip,add2,passwd))
#		print result
		if "No route to host" in result:
			print "-"*100
			print "\033[33;40;1m服务器 %s 连接失败!\033[0m" % (ip)
		if "Permission denied (publickey)" in result:
			print "-"*100
			print "\033[33;40;1m服务器 %s 公钥登录失败!\033[0m" % (ip)
			return
		if "root@%s\'s password:" % (ip) in result:
			print "-"*100
			print "\033[33;40;1m服务器 %s 公钥错误,请检查!\033[0m" % (ip)
		else:
			print "-"*100
			print result
			return

	if method == 'password':
		try:
			passwd = mydecode.mydecode(passwd)
		except:
			print "\033[33;40;1m%s 不是一个有效的密码,服务器IP为: %s \033[0m" % (passwd,ip)
			return
		status, result = commands.getstatusoutput("%s/include/expect/traffic_password %s root@%s:%s %s" % (WORKDIR,add1,ip,add2,passwd))
		if "No route to host" in result:
			print "-"*100
			print "\033[33;40;1m服务器 %s 连接失败!\033[0m" % (ip)
		if "Permission denied" in result:
			if "Permission denied (publickey)" in result:
				print "-"*100
				print "\033[33;40;1m服务器 %s 禁用密码登录,请使用公钥!\033[0m" % (ip)
			else:
				print "-"*100
				print "\033[33;40;1m服务器 %s 密码错误,请检查!\033[0m" % (ip)
		else:
			print "-"*100
			print result

def execute_command(cmd,ip,passwd,method):
	if method == 'publickey':
		status, result = commands.getstatusoutput("%s/include/expect/base_publickey %s %s \"%s\"" % (WORKDIR,ip,passwd,cmd))

		if "No route to host" in result:
			print "-"*100
			print "\033[33;40;1m服务器 %s 连接失败!\033[0m" % (ip)
		if "Permission denied (publickey)" in result:
			print "-"*100
			print "\033[33;40;1m服务器 %s 公钥登录失败!\033[0m" % (ip)
			return
		if "root@%s\'s password:" % (ip) in result:
			print "-"*100
			print "\033[33;40;1m服务器 %s 上的公钥错误,请检查!\033[0m" % (ip)
		else:
			print "-"*100
			print result
			return

	if method == 'password':
		try:
			passwd = mydecode.mydecode(passwd)
		except:
			print "\033[33;40;1m%s 不是一个有效的密码,服务器IP为: %s \033[0m" % (passwd,ip)
			return
		status, result = commands.getstatusoutput("%s/include/expect/base_password %s %s \"%s\"" % (WORKDIR,ip,passwd,cmd))
		if "No route to host" in result:
			print "-"*100
			print "\033[33;40;1m服务器 %s 连接失败!\033[0m" % (ip)
		if "Permission denied" in result:
			if "Permission denied (publickey)" in result:
				print "-"*100
				print "\033[33;40;1m服务器 %s 禁用密码登录,请使用公钥!\033[0m" % (ip)
			else:
				print "-"*100
				print "\033[33;40;1m服务器 %s 密码错误,请检查!\033[0m" % (ip)
		else:
			print "-"*100
			print result
			return
