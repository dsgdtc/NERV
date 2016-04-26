# -*- coding:utf-8 -*-
import base64

def mydecode(pwd):
	s1 = bytearray(str(pwd).encode("gbk"))
	s2 = bytearray(len(s1))
	for i in range(len(s1)):
		s2[i] = s1[i] - 3
	s3 = base64.decodestring(str(s2))
	return s3
#	print "The plaintext is %s " % (s3)

#pwd = raw_input("imput Encrypted password:")
#print mydecode(pwd)
