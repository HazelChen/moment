#-*- coding:utf-8 -*-
import sys, time, pymysql, datetime

connection = pymysql.connect('localhost', 'root', 'root', 'moment');

room_cursor = connection.cursor()
room_cursor.execute('SELECT * FROM `moment_room`')
room_list = room_cursor.fetchall()

with connection:
	while True:
		for room in room_list:
			room_id = room[0]
			duration = room[1]
			word_cursor = connection.cursor()
			word_cursor.execute('DELETE FROM `moment_word` WHERE `room_id`= %s AND (now() - `timestamp`) >= 300', [room_id])
			connection.commit()
		time.sleep(60)