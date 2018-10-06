#!/usr/bin/env python
import getpass
username = raw_input("username:")
password = getpass.getpass("passeord:")

if username == "chen" and  password == "5920":
        print "successed login"

else:
    print "nologin"