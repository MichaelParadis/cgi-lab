#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
import os
import json
from urllib.parse import parse_qs

print("Content-Type: text/html\n")
print()
print("<!doctype html>")
print("<head>")
print("<title>Hello</title>")
print("<style> pre {white-space:pre-wrap; word-wrap:break_word;}")
print("</style>")
print("</head>")
print("<h2>Hello World</h2>")
# cgi.print_environ()
print("<dl>")
print("<dt>QUERY_STRING</dt>")
print("<dd>")
print(parse_qs(os.environ.get("QUERY_STRING")))
print("</dd>")
print("</dl>")

print("<pre>")
env_json = {}
for key,value in os.environ.items():
	env_json[key] = value
print(json.dumps(env_json))
print("</pre>")

