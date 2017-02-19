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
    ## Defining constants
    self.DINNERS_RANGE = range(12,18)
    self.LIMIT_PEOPLE_FOR_SLOT = 3
    ## Other vars
    self.peolpe_in_schedule = []
    ##
    ## The following is a class logic
    ##
    self.dinners_timeslots = [str(i) for i in self.DINNERS_RANGE]
    ##
    ## Type of self.dinners_schedule is dict:
    ## The structure of self.dinners_schedule: {timeslot0: (set of people), timeslot1: (set of people) ...}
    self.dinners_schedule = {} 
    for i in self.dinners_timeslots:
      self.dinners_schedule[i] = ()

  def sched_update(self, who, desired_timeslot):
    if len(self.dinners_schedule[desired_timeslot]) < self.LIMIT_PEOPLE_FOR_SLOT:
      if who not in self.peolpe_in_schedule:
        self.peolpe_in_schedule.append(who)
        self.dinners_schedule[desired_timeslot]+=who,
      else:
        self.dinners_schedule[desired_timeslot]+=who,
        #and need remove previos record in schedule

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

  d.sched_update('MRe', '15')
  print(d.dinners_schedule)
  d.shed_view()
  d.sched_update('Ar', '15')
  print(d.dinners_schedule)
  d.shed_view()
  d.sched_update('Ps', '15')
  print(d.dinners_schedule)
  d.shed_view()
  d.sched_update('Nm', '15')
  print(d.dinners_schedule)
  d.shed_view()
