#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ldap3 import Server, Connection, ALL, NTLM

def auth_check(username, passwd):
  server = Server('mgts.corp.net')
  conn = Connection(server, user="mgts\\"+username, 
                    password=passwd, authentication="NTLM")
  auth_result = conn.bind()
  return auth_result


if __name__=='__main__':
  username = ['testuser', 'testpass0']
  password = ['testuser1', 'testpass1']
  for i in range(2):
    print(username[i], password[i], ':', auth_check(username[i], password[i]))

