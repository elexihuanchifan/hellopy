import pymysql

conn = pymysql.connect(host='localhost' , port=3306, user='vamei' , password='vameiisgood' , db='villa',charset='UTF8')
cur = conn.cursor()
cur.execute("CREATE TABLE user (id int PRIMARY KEY, name  varchar(20))")
cur.close()
conn.commit()
conn.close()