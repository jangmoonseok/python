import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="python", port=3305, database="python", charset="utf8")

cur = conn.cursor()
sql = "insert into emp values(5,'5','5','5')"
cur.execute(sql)

print(cur.rowcount)
conn.commit()

cur.close()
conn.close()