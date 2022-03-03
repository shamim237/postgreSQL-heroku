import psycopg2

conn = psycopg2.connect(database="zibew_chatbot",
						user='postgres', password='shamim237x',
						host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()


sql = '''CREATE TABLE chatbot_2(
name text NOT NULL,\
mobile int NOT NULL,\
email varchar(40) NOT NULL,\
age int NOT NULL,\
weight int NOT NULL,\
temp real NOT NULL);'''


cursor.execute(sql)

sql2 = '''COPY chatbot_2(name,mobile,\
email,age,weight,temp) 
FROM 'D:/others/MS_Chatbot/flow/botbuilder-samples/samples/python/44.prompt-for-user-input/dataset.csv'
DELIMITER ','
CSV HEADER;'''

cursor.execute(sql2)

sql3 = '''select * from chatbot_2;'''
cursor.execute(sql3)
for i in cursor.fetchall():
	print(i)

conn.commit()
conn.close()
