import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="python", port=3305, database="python", charset="utf8")

cur = conn.cursor()


sql = """
    delete from emp where e_id = '6'
"""
cnt = cur.execute(sql)

print(cnt)
conn.commit()

cur.close()
conn.close()