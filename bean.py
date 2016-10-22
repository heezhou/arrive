#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import *
import pymysql
from decouple import config

#db = SqliteDatabase('analyst.db')
db = MySQLDatabase(config('DATABASE'),host = config('HOST'),user=config('DB_USER_NAME'),password=config('DB_PASSWORD'),charset='utf8mb4')
db.connect()
class Person(Model):
	name = CharField()
	birthday = DateField()
	is_relative = BooleanField()
	
	class Meta:
		database = db

class Pet(Model):
	owner = ForeignKeyField(Person,related_name='pets')
	name = CharField()
	animal_type = CharField()
	
	class Meta:
		database = db

class DailyExpense(Model):
	pid = CharField(unique=True)
	cardno = CharField()
	exDate = CharField()
	exTime = CharField()
	currency = CharField()
	exRecord = CharField()
	fee = FloatField()
	
	class Meta:
		database = db




if __name__=='__main__':
	for de in DailyExpense.select():
		print(de.pid,de.cardno,de.exDate,de.exTime,de.currency,de.exRecord,de.fee)
#db.create_tables([DailyExpense])
# uncle_bob = Person(name='Bob',birthday=date(1960,7,1),is_relative=True)
# uncle_bob.save()
# sara = Person.create(name='Sara',birthday=date(1987,3,3),is_relative=False)
# sara.save()

