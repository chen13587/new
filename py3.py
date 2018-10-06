#!/usr/bin/env python
import getpass
name = raw_input("username: ")
ps = getpass.getpass("password: ") 
if name == "chen" and ps == "5920":
  print "login successed"

else:
  print "login failed"


