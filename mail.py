#!/usr/bin/env python
# -*- coding: utf-8 -*-

from imbox import Imbox
from bs4 import BeautifulSoup
from datetime import date,datetime
import time
from bean import DailyExpense
import when 
from apscheduler.schedulers.background import BackgroundScheduler
from decouple import config
#Messages sent from 
#strdate = '2016-07-16'
#print(when.yesterday())
#date_time = datetime.strptime(strdate,'%Y-%m-%d').date()
def getmaildata():
	print('=====Get Mail Data %s====='%datetime.now())
	imbox = Imbox(config('IMAP_ADDRESS'),
			username=config('USER_NAME'),
			password=config('PASSWORD'),
			ssl=True,
			ssl_context=None)
	messages_from = imbox.messages(date__gt=when.yesterday(),sent_from=config('SENT_FROM'))
	#messages_from = imbox.messages(sent_from='ccsvc@message.cmbchina.com')
	ldata = []
	c,n = 0,0	
	#解析数据
	for uid,message in messages_from:
		html = str(message.body['html'])
		a = html[2:-2]
		soup = BeautifulSoup(a,'html.parser')
		b = soup.find_all('font')
		for s in b:
			if s.string is not None:
				ldata.append(s.string)
	print('=====Praser Data Success  Size:%s ====='%str(len(ldata)/6))
	#写入数据库
	while n < len(ldata)/6:
		try:
			pid =ldata[1+c]+ldata[2+c].replace(':','')
			de = DailyExpense.create(cardno=ldata[0+c],exDate=ldata[1+c],exTime=ldata[2+c],currency=ldata[3+c],exRecord=ldata[4+c],fee=float(ldata[5+c].replace(',','')),pid=pid)
			de.save()
		except Exception as e:
			print(e)
		n,c = n+1,c+6

if __name__ == '__main__':
	getmaildata()



