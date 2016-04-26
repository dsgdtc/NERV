# -*- coding:utf-8 -*-
from init import ReadConf
from include import function
show_server=function.Show_Server()
send_files=function.Send_Files()
execute_command=function.Execute_Command()
add_server=function.Add_Server()

class ShowMenu(ReadConf):
	def __init__(self,flag):
		self.flag = flag
		#pass
	def main_menu(self):
		print """\033[1;34m
主菜单
	1:分发文件
	2:执行命令
	3:查看所有服务器列表
	0:退出\033[0m
    	"""
#	4:新增删除服务器
#	5:增加删除修改服务器组
	def send_files(self):
		while "self.flag":
			print """\033[1;34m
	1:向服务器传送文件
	2:向服务器传送cmd.sh脚本
	0:返回\033[0m
		"""
			choice = function.choose()
			choice_list = ['1','2','0']
			if choice not in choice_list:
				print "\033[33;40;1m没有这个选项,返回主菜单!\033[0m"
				self.flag = 0
				break
			if choice == '1':
				send_files.send_file()
			if choice == '2':
				send_files.send_cmdfile()
			if choice == '0':
				self.flag = 0
				break	
	def execute_cmd(self):
		while "self.flag":
			print """\033[1;34m
	1:在服务器端执行命令
	2:在服务器端执行cmd.sh脚本(root权限执行)
	0:返回\033[0m
		"""
			choice = function.choose()
			choice_list = ['1','2','0']
			if choice not in choice_list:
				print "\033[33;40;1m没有这个选项,返回主菜单!\033[0m"
				self.flag = 0
				break
			if choice == '1':
				execute_command.execute()
			if choice == '2':
				execute_command.execute_cmd()
			if choice == '0':
				self.flag = 0
				break
	def show_server(self):
		while "self.flag":
			print """\033[1;34m
	1:查看所有组
	2:查看所有服务器
	0:返回\033[0m
        """
			choice = function.choose()
			choice_list = ['1','2','0']	
			if choice not in choice_list:
				print "\033[33;40;1m没有这个选项,返回主菜单!\033[0m"
				self.flag = 0
				break
			if choice == '1':
				show_server.show_all_group()
			if choice == '2':
				show_server.show_all_server()
			if choice == '0':
				self.flag = 0
				break
	def add_server(self):
		while "self.flag":
			print """\033[1;34m
	1:增加
	2:删除
	0:返回\033[0m
        """
			choice = function.choose()
			choice_list = ['1','2','0']	
			if choice not in choice_list:
				print "\033[33;40;1m没有这个选项,返回主菜单!\033[0m"
				self.flag = 0
				break
			if choice == '1':
				add_server.add_server()
			if choice == '2':
				show_server.show_all_server()
			if choice == '0':
				self.flag = 0
				break
	def add_server_group(self):
		print """\033[1;34m
		选择组用choose_group这个函数，还是得重写,列出ID和组名
		len(group_list)+1:新增一个组
			1:查看组中的服务器
			2:向组中添加服务器
			3:从组中删除服务器
			4:删除此组(不包括组下的服务器)
			5:删除此组(包括组下的服务器)
			6:修改此组的名字
			0:返回
		0:返回\033[0m
		"""

	def choose_group(self):
		print "\033[1;34m选择组:"
		for i in self.read_group_dict().keys():
			#print "%s:"%(i),self.read_group_dict().get(i).keys()[0],"	该组下ip示例:",self.read_group_dict().get(i).values()[0][:3]
			print "%s:"%(i),self.read_group_dict().get(i).keys()[0]
			print "	该组下ip举例:",self.read_group_dict().get(i).values()[0][:3]
		print "\033[0m"
#		print self.read_group_dict(),"\033[0m"
#showmenu=ShowMenu()
#showmenu.choose_group()
