#!/usr/bin/env python3
import cgi
import cgitb
import os
cgitb.enable()
from secret import username, password
from templates import login_page, secret_page, after_login_incorrect
print("Content-Type: text/html")


c_username = ""
c_password = ""
cookie_string = os.environ.get("HTTP_COOKIE")
cookie_pairs = cookie_string.split(';')
for pair in cookie_pairs:
	(key,value) = pair.split('=')
	if 'username' in key:
		c_username = value
	if 'password' in key:
		c_password = value

if c_password == password and c_username == username:
	print('\n\n')
	print(secret_page(username, password))

elif os.environ.get("REQUEST_METHOD", "GET") == "POST":
	# print form post data
	form = cgi.FieldStorage()
	f_username = form.getvalue('username')
	f_password = form.getvalue('password')
	if f_username == username and f_password == password:
		print("Set-Cookie: username={};".format(username))
		print("Set-Cookie: password={};".format(password))
		print("\n\n")
		print(secret_page(username, password))
	else:
		print("\n\n")
		print(after_login_incorrect())

else:
	print("\n\n")
	print(login_page())