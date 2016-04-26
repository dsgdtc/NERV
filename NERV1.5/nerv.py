# -*- coding:utf-8 -*-
import os,sys
from include import menu
from include import function
from include import tab
from include import headline 
showmenu=menu.ShowMenu(0)
showserver=function.Show_Server()
headline
#print """
#-------------------------------------------------------------------------------------------------------		
#	THIS IS A BEAUTIFUL WELCOM SCREEN ！
#-------------------------------------------------------------------------------------------------------		
#	"""

while True:
	showmenu.main_menu()
	try:
		choice = function.choose()
		choice_list = ['1','2','3','0','exit','quit']
		if choice not in choice_list:
			print "\033[33;40;1m没有这个选项,返回主菜单!\033[0m" 
			continue
		if choice == '1':
			showmenu.flag = 1
			showmenu.send_files()
		if choice == '2':
			showmenu.flag = 1
			showmenu.execute_cmd()
		if choice == '3':
			showmenu.flag = 1
			showmenu.show_server()
#		if choice == '4':
#			showmenu.flag = 1
#			showmenu.add_server()
#		if choice == '5':
#			os._exit(0)
		if choice == '0':
			print "\033[33;40;1m谢谢使用^_^\033[0m "
			os._exit(0)
		if choice == 'exit':
			print "\033[33;40;1m谢谢使用^_^\033[0m "
			os._exit(0)
		if choice == 'quit':
			print "\033[33;40;1m谢谢使用^_^\033[0m "
			os._exit(0)
	except KeyError as e:
		print "\033[33;40;1m选择错误! %s \033[0m "
		sys.exit()
	except KeyboardInterrupt:
		print "\n\033[33;40;1m退出.\033[0m "
		sys.exit()
	except EOFError:
		print "\n\033[33;40;1m退出.\033[0m "
	except ValueError as e:
		print "\033[33;40;1m选择错误! %s \033[0m "
	except AttributeError as e:
		print "\033[33;40;1m没有这个选项,返回主菜单! \033[0m "
	except IOError as e:
		print "\033[33;40;1m请在主目录下运行python nerv.py \033[0m "
#	except AttributeError:
#		print '\n\033[31;1mSome error happend,please send bug to dsgdtc@163.com AttributeError\033[0m'
#	else:
#		print "\033[33;40;1m遇到了一些没有想到的BUG,请提交到dsgdtc@163.com. \033[0m "
