# -*- coding:utf-8 -*-
import os
import sys
import multiprocessing
import time
import commands
from init import ReadConf
import init
import Commands
WORKDIR = init.WORKDIR 
def choose():
	choose = raw_input("\033[0;32minput your choice:\033[0m").strip()
	return choose

class Print_Group(ReadConf):
	def Print_Group(self):
		dict_sort = {}
		dict_sort = sorted(self.read_group_dict().iteritems(), key=lambda d:int(d[0]), reverse = False)#排序转换之后是个列表,不再是字典了,要注意
#		print dict_sort
		print "\033[1;34m"
		for i in range(len(dict_sort)):
			print "	%s:" % dict_sort[i][0] ,dict_sort[i][1].keys()[0]#dict_sort.get(i).keys()[0]
		print "	0: 返回\033[0m"
#test=Print_Group()
#test.Print_Group()

class Show_Server(ReadConf,Print_Group):

	def show_all_server(self):
		for server in self.read_server():
			print server[1]
		print "\033[1;36m共%s台服务器在控制中\033[0m" % (len(self.read_server()))
		raw_input()

	def show_all_group(self):
		self.Print_Group()
		print "\033[1;36m共%s个组在控制中\033[0m" % (len(self.read_group_dict()))
		group_num = raw_input("\033[0;32minput your choice:\033[0m").strip()
		if group_num == '0':
			return	
		else:
			print "\033[1;36m%s里边有%s台服务器:\033[0m" % (self.read_group_dict().get(group_num).keys()[0],len(self.read_group_dict().get(group_num).values()[0]))
			print self.read_group_dict().get(group_num).values()[0]
			raw_input()

class Send_Files(Show_Server):

	def send_file(self):
		self.Print_Group()
		group_num = raw_input("\033[0;32m要向哪个组分发文件?:\033[0m").strip()
		if group_num == '0':
			pass
		else:
			print "\033[1;36m%s里边有以下服务器:%s\033[0m" % (self.read_group_dict().get(group_num).keys()[0], self.read_group_dict().get(group_num).values()[0])
			add1=raw_input("\033[0;32m本地文件(绝对路径):\033[0m").strip()
			if add1 == 'quit' or add1 == 'exit':return
			add2=raw_input("\033[0;32m远端服务器目的地址(绝对路径):\033[0m").strip()
			if add2 == 'quit' or add2 == 'exit':return
			pool = multiprocessing.Pool(processes=20)
			for server in self.read_group_dict().get(group_num).values()[0]:
				for id in self.read_server_dict().keys(): 
					if self.read_server_dict()[id].get(server):
						pool.apply_async(Commands.traffic_file, (add1,add2,server,self.read_server_dict()[id].get(server)[0],self.read_server_dict()[id].get(server)[1], ))

			pool.close()
			pool.join()

	def send_cmdfile(self):	
		self.Print_Group()
		group_num = raw_input("\033[0;32m要向哪个组分发cmd文件?:[ cmd.sh文件分发到目录/root/script/下 ]\033[0m").strip()
		if group_num == '0':
			pass
		else:
			print "\033[1;36m%s里边有以下服务器:%s\033[0m" % (self.read_group_dict().get(group_num).keys()[0], self.read_group_dict().get(group_num).values()[0])
			sure = raw_input("\033[0;32m确定分发cmd.sh到各服务器/root/script/下[ Y/N Y为缺省值 ]:\033[0m").strip()
			add1 = "%s/cmd.sh" % (WORKDIR)
			add2 = "/root/script/"
			pool = multiprocessing.Pool(processes=20)
			for server in self.read_group_dict().get(group_num).values()[0]:
				for id in self.read_server_dict().keys():
					if self.read_server_dict()[id].get(server):
						pool.apply_async(Commands.traffic_file, (add1,add2,server,self.read_server_dict()[id].get(server)[0],self.read_server_dict()[id].get(server)[1], ))

			pool.close()
			pool.join()
			
class Execute_Command(Show_Server):

	def execute(self):
		self.Print_Group()
		group_num = raw_input("\033[0;32m要控制哪个组?:\033[0m").strip()
		if group_num == '0':
			pass
		else:
			print "\033[1;36m%s里边有以下服务器:%s\033[0m" % (self.read_group_dict().get(group_num).keys()[0], self.read_group_dict().get(group_num).values()[0])
			cmd=raw_input("\033[0;32m输入要执行的命令(不能带引号):\033[0m").strip()
			pool = multiprocessing.Pool(processes=20)
			for server in self.read_group_dict().get(group_num).values()[0]:
				for id in self.read_server_dict().keys():
					if self.read_server_dict()[id].get(server):
						pool.apply_async(Commands.execute_command, (cmd,server,self.read_server_dict()[id].get(server)[0],self.read_server_dict()[id].get(server)[1], ))
			pool.close()
			pool.join()

	def execute_cmd(self):
		self.Print_Group()
		cmd = "/root/script/cmd.sh"
		group_num = raw_input("\033[0;32m要对那些组的服务器执行cmd.sh脚本?:\033[0m").strip()
		if group_num == '0':
			pass
		else:
			print "\033[1;36m%s里边有以下服务器:%s\033[0m" % (self.read_group_dict().get(group_num).keys()[0], self.read_group_dict().get(group_num).values()[0])
			sure = raw_input("\033[0;32m确定到服务器上执行cmd.sh脚本(root用户,用于执行cmd.sh脚本)[ Y/N Y为缺省值 ]:\033[0m").strip()
			pool = multiprocessing.Pool(processes=20)
			for server in self.read_group_dict().get(group_num).values()[0]:
				for id in self.read_server_dict().keys():
					if self.read_server_dict()[id].get(server):
						pool.apply_async(Commands.execute_command, (cmd,server,self.read_server_dict()[id].get(server)[0],self.read_server_dict()[id].get(server)[1], ))
			pool.close()
			pool.join()

class Add_Server(Show_Server):

	def add_server(self):
		serial_id = len(self.read_server()) + 1 
#		print serial_id
		new_ip = raw_input("\033[0;32m服务器IP地址:\033[0m").strip()
		new_pwd = raw_input("\033[0;32m服务器root密码(不知道写123456):\033[0m").strip()
		ssh_method = raw_input("\033[0;32m服务器登录方式,密码或公钥认证方式[ password/publickey ]:\033[0m").strip()
		if ssh_method not in [ "password", "publickey" ]:
			print '\033[33;40;1mWrong option!\033[0m '
			return
		f = file("%s/conf/server.conf" % (WORKDIR),'a')
		f.write("%s\t%s\t%s\t%s" % (serial_id, new_ip, new_pwd, ssh_method))
		f.close()
		raw_input("\033[0;32m重新执行程序后生效(敲任意键退出)...\033[0m")
		time.sleep(0.2)
		return
#		os._exit(0)

	def del_server(self):
		pass
