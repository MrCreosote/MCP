#!/usr/bin/env python

from mlog import mlog

################################################################################

m = mlog("pipeline")
print "log_level = " + str(m.get_log_level())

m.log_message(2, "my test message at log level 2 with no constraints")
m.log_message(3, "my test message at log level 2 with no constraints")
m.log_message(4, "my test message at log level 2 with no constraints")

################################################################################

log_constraints = { 'job' : '3', 'stage' : '350' }
m = mlog("pipeline", log_constraints)
print "log_level = " + str(m.get_log_level())

m.log_message(2, "my test message at log level 2 with constraints job=3 and stage=350");
m.log_message(3, "my test message at log level 3 with constraints job=3 and stage=350");
m.log_message(4, "my test message at log level 4 with constraints job=3 and stage=350");

################################################################################

m.set_log_level(5)
print "log_level = " + str(m.get_log_level())

m.log_message(2, "my test message at log level 2 with constraints job=3 and stage=350");
m.log_message(3, "my test message at log level 3 with constraints job=3 and stage=350");
m.log_message(4, "my test message at log level 4 with constraints job=3 and stage=350");

################################################################################

#m.log_message('emergency', "this program is finished")
