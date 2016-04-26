# -*- coding:utf-8 -*-
import os
import sys
import re
WORKDIR = os.path.dirname(os.path.dirname(__file__))
#print WORKDIR
#WORKDIR = os.path.abspath('.') 
global CHEKC_FLAG
CHECK_FLAG = 0

class ReadConf():

	#把服务器文件读成列表的格式使用
	def read_server(self):
		server_list=[]
		with open ("%s/conf/server.conf" % WORKDIR) as f:
			for line in f.readlines():
				p = re.compile(r'^#')
				if not p.match(line):
					server_list.append(line.split())
#		print server_list
		return server_list
	#后来我发现,服务器列表我需要以字典的方式使用,于是又写了下边这段函数.....也是字典套字典,就当时为以后扩展做准备吧,{1:{ip:[]}}
	def read_server_dict(self):
		server_dict={}
		with open ("%s/conf/server.conf" % WORKDIR) as f:
			for line in f:
				p = re.compile(r'^#')
				if not p.match(line):
					server_dict[line.split()[0]] = {line.split()[1]:line.split()[2:]} 
		return server_dict

	def read_group_dict(self):
		group_dict={}
		with open ("%s/conf/group.conf" % WORKDIR) as f:
			for line in f:
				p = re.compile(r'^#')
				if not p.match(line):
					group_dict[line.split()[0]] = {line.split()[1]:line.split()[2:]}
		return group_dict



readconf = ReadConf()
def check_server_ip():
	result = []
	def check_ip(text):
		p = re.compile(r'(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])')
		if p.match(text):
			pass 
		else:
			global CHECK_FLAG
			CHECK_FLAG = '1'
			print "\033[1;35m%s  不是合法的IP! 请修改./conf/server.conf文件\033[0m" % text

	for server in readconf.read_server():
		check_ip(server[1])

def check_ssh_method():
	for server in readconf.read_server():
		if server[3] not in [ "password", "publickey" ]:
			global CHECK_FLAG
			CHECK_FLAG = '1'
			print "\033[1;35m%s  不支持这种SSH认证方式,请修改./conf/server.conf文件\033[0m" % server[3]

def check_group_id():
	global CHECK_FLAG
	for group_id in readconf.read_group_dict().keys():
		if group_id.isdigit():
			pass
		else:
			CHECK_FLAG = '1'
			#print "\033[1;35m%s  组ID必须是数字,请修改./conf/group.conf文件\033[0m" % group_id
			print "\033[1;35m组ID必须是数字,请修改./conf/group.conf文件\033[0m"

def check_groupid_uniq():
	group_id_list = []
	with open ("%s/conf/group.conf" % WORKDIR) as f:
		for line in f:
			p = re.compile(r'^#')
			if not p.match(line):
				group_id_list.append(line.split()[0])
	group_id_uniq = set(group_id_list)
	for item in group_id_uniq:
		if group_id_list.count(item) > 1:
			global CHECK_FLAG
			CHECK_FLAG = '1'
			print "\033[1;35m组ID  %s  存在 %d 个,请修改./conf/group.conf\033[0m" % (item,group_id_list.count(item))
	
def check_server_lookup():
	server_all = []
	for server in readconf.read_server():
		server_all.append(server[1])
	for group_link_server in readconf.read_group_dict().values():
		for ip in group_link_server.values()[0]:
			if ip in server_all:
				pass
			else:
				global CHECK_FLAG
				CHECK_FLAG = '1'
				print "\033[1;35m%s  不在./conf/server.conf中,请添加\033[0m" % ip

def check_server_uniq():
	server_all = []
	for server in readconf.read_server():
		server_all.append(server[1])
	server_uniq = set(server_all)
	for item in server_uniq:
		if server_all.count(item) > 1:
			global CHECK_FLAG
			CHECK_FLAG = '1'
			print "\033[1;35m%s  存在 %d 个,请修改./conf/server.conf\033[0m" % (item,server_all.count(item))
#print read.read_server()
#read.read_group()
#print type(read.read_server_dict)
#print read.read_server_dict().values()[0]['192.168.80.22']
check_server_ip()
check_ssh_method()
check_group_id()
check_server_lookup()
check_server_uniq()
check_groupid_uniq()

if CHECK_FLAG == '1':
	os._exit(0)
