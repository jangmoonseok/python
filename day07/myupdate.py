import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="python", port=3305, database="python", charset="utf8")

cur = conn.cursor()
e_id = "6"
e_name = "5"
sex = "5"
addr = "5"

sql = f"""
    update emp set
        e_name = '{e_name}',
        sex = '{sex}',
        addr = '{addr}'
    where e_id = '{e_id}'
"""
cnt = cur.execute(sql)

print(cnt)
conn.commit()

cur.close()
conn.close()