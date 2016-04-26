import base64
s1 = raw_input("imput a password:")
s2 = base64.encodestring(s1)
print "-"*100
print "your password is: %s" % (s1)
print "the encoded password is %s" %(s2)
print "-"*100
