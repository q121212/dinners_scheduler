#!/usr/bin/python3
# -*- coding: utf-8 -*-

from ldap3 import Server, Connection, ALL, NTLM

def auth_check(username, passwd):
  server = Server('mgts.corp.net')
  conn = Connection(server, user="mgts\\"+username, 
                    password=passwd, authentication="NTLM")
  auth_result = conn.bind()
  return auth_result

class Dinners:
  def __init__(self):
    self.dinners_range = range(12,18)
    self.limit_people_for_slot = 3
    self.dinners_timeslots = [str(i) for i in self.dinners_range]
    self.dinners_schedule = {}
    for i in self.dinners_timeslots:
      self.dinners_schedule[i] = []

  def sched_update(self, who, desired_timeslot):
    print(self.dinners_schedule[desired_timeslot])
    if len(self.dinners_schedule[desired_timeslot]) < self.limit_people_for_slot:
      self.dinners_schedule[desired_timeslot].append(who)

  def shed_view(self):
    for key in sorted(self.dinners_schedule):
      print(key, self.dinners_schedule[key])

if __name__=='__main__':
  username = ['testuser', 'testpass0']
  password = ['testuser1', 'testpass1']
  for i in range(2):
    print(username[i], password[i], ':', auth_check(username[i], password[i]))

  d=Dinners()
  print(d.dinners_schedule)
  d.sched_update('MRe', '13')
  print(d.dinners_schedule)
  d.shed_view()
  d.sched_update('Ar', '13')
  print(d.dinners_schedule)
  d.shed_view()
  d.sched_update('Ps', '13')
  print(d.dinners_schedule)
  d.shed_view()
  d.sched_update('Nm', '13')
  print(d.dinners_schedule)
  d.shed_view()
