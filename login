#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# File: login

import cgitb; cgitb.enable()
import page_functions
import cgi
form = cgi.FieldStorage()
username = form.getfirst('username', '')
password = form.getfirst('password', None)
result = ''
what_to_print, chk= page_functions.loginBox(username, password)
if username != None and password != None and chk:
   result = '<p>User does not exit or username/password wrong</p>'

print r"""Content-Type: text/html;charset=utf-8

<html>
%s
<body>
%s
</br>
%s
%s
</body>
</html>
""" % (page_functions.header(), page_functions.topLinks(),
result, what_to_print)
