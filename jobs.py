#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
import mail


#任务调度
scheduler = BackgroundScheduler()
scheduler.add_job(mail.getmaildata, 'interval', days=1)
scheduler.start()
print('Mail Job Start Working ...')

try:
    # This is here to simulate application activity (which keeps the main thread alive).
    while True:
        time.sleep(5)
except (KeyboardInterrupt, SystemExit):
    # Not strictly necessary if daemonic mode is enabled but should be done if possible
    scheduler.shutdown()