#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# File: login

import cgitb; cgitb.enable()
import page_functions
import cgi
form = cgi.FieldStorage()
username = form.getfirst('username', '')
password = form.getfirst('password', None)

import MySQLdb
db = MySQLdb.connect(host='localhost', port=1234,
                     user='root', passwd='', db='quickShare')
cursor = db.cursor()
db_pass = ''
errors = ''
if username != '':
   if (cursor.execute("SELECT password FROM User WHERE username='%s'" % username) >= 1):
      db_pass = cursor.fetchone()[0]
   else:
      errors += 'The user name does not exist.</br>'    
what_to_print, chk= page_functions.loginBox(username, password, db_pass)
if chk and username and password:
   errors = 'The password is incorrect.</br>'

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
errors, what_to_print)
