#!/bin/bash
echo "Wait a few seconds..."
sleep 2
#log=0
#if [ $log = 0 ]; then
#	exec >> /dev/null #2>&1
#fi

rpm -q expect tcl  
#rpm -q expect tcl &>/dev/null 
if [ $? -eq 0 ] ;then
	echo "Now you can run \"python nerv.py\" to manage your servers!"
	echo "if it not works,send your question to fangcun727@aliyun.com"
else
	rpm -ivh "$PWD"/dependency/tcl-8.5.7-6.el6.x86_64.rpm 
	rpm -ivh "$PWD"/dependency/expect-5.44.1.15-5.el6_4.x86_64.rpm 
	echo "Now you can run \"python nerv.py\" to manage your servers!"
	echo "if it not works,send your question to fangcun727@aliyun.com"
fi
