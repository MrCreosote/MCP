'''
Created on Sep 30, 2013

@author: gaprice@lbl.gov
'''

import mlog
import sys
import time

log = mlog.mlog("LotsaLogs", authuser=True, module=True, method=True,
                call_id=True, ip_address=True)

t = time.time()

for i in xrange(int(sys.argv[1])):
    log.log_message(6, "Here's a friggin log message for ya, hoser",
        'Mind yer own damned business', 'SomeModule', 'SomeMethod',
        134515126161, "0.0.0.0")

print time.time() - t
