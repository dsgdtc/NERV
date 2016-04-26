# -*- coding:utf-8 -*-
import textwrap,Termina_size

HeadLine='''\033[32;1m
|=============================================================================================================================|
|															      |
|						         NERV 1.4							      |
|                                                    Small and Light							      |
|														              |
|															      |				
|\tThank you for use NERV 1.4 management console,you will be able to manage many servers through this small and          |
|\tlight software.													      |
|															      |
\033[31;1m|\tPlease be careful with your opreations because right now the key of managing the whole network is in your hand.	      |	
|\tYou must be very clear about any instructions you input before you send them to this console.			      |
|\t注意,你拥有所有的root权限！                                                                                           |\033[32;1m 
|															      |
|															      |
|                  								Report bug:  fangcun727@aliyun.com            |
|_____________________________________________________________________________________________________________________________|
\033[0m'''

HeadLine100='''\033[32;1m
|==============================================================================================|
|                                                                                              |
|                                           NERV 1.4                                           |
|                                       Small and Light                                        |
|                                                                                              |
|   Thank you for use NERV 1.4 management console,you will be able to manage many servers      |
|   through this small and light software.                                                     |     
|\t                                                                                       |\033[0m
\033[31;1m|   Please be careful with your opreations because right now the key of managing the whole     | 
|   network is in your hand.You must be very clear about any instructions you input befor      | 
|   you send them to this console.                                                             |
|   注意,你拥有所有的root权限！                                                                |\033[32;1m
|                                                                                              |
|                                                 Report bug: fangcun727@aliyun.com            |
|______________________________________________________________________________________________|
\033[0m'''

HeadLine65='''\033[32;1m
|===============================================================|
|                                                               |
|                             NERV 1.4                           |
|                         Small and Light                       |
|                                                               |
|   Thank you for use NERV 1.4 management console,you will be   |
|   able to manage many servers through this small              |
|   and light software.                                         |
|\t                                                        |
\033[31;1m|   Please be careful with your opreations because right now    |
|   the key of managing the whole network is in your hand.      |
|   You must be very clear about any instructions you input     |
|   befor you send them to this console.                        |
|   注意,你拥有所有的root权限！                                 |\033[32;1m
|                                                               |
|                       Report bug: fangcun727@aliyun.com       |
|_______________________________________________________________|
\033[0m'''
def head_line():
	T_size = Termina_size.terminal_size()
	if T_size[0] >= 127:
		print HeadLine
	elif T_size[0] >= 100:
		print HeadLine100 
	else: 
		print HeadLine65
		#print T_size

head_line()


