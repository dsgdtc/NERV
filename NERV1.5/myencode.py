import base64
def myencode():
	pwd = raw_input("imput your password:")
	s1 = base64.encodestring(pwd)
#	print "base64:",s1

	s2 = bytearray(str(s1).encode("gbk"))
	s3 = bytearray(len(s2))
	for i in range(len(s2)):
		s3[i] = s2[i] + 3
	print "encoded password is: %s " % (s3)

myencode()
