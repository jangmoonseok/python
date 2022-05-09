import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="python", port=3305, database="python", charset="utf8")

cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute("select * from emp")
rows = cur.fetchall()

print(rows)


cur.close()
conn.close()
