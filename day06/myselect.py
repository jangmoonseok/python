# import mariadb
# import sys
#
# try:
#     conn = mariadb.connect(
#         user = "root",
#         password = "python",
#         host ="127.0.0.1",
#         port=3305,
#         database="python"
#     )
# except mariadb.Error as e:
#     print(e)
#     sys.exit(1)
#
# cur = conn.cursor()
# cur.execute("select * from emp")
# resultset = cur.fetchall()
#
# for i in resultset:
#     print(i)
# conn.close()
import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="python", port=3305, database="python", charset="utf8")


cur = conn.cursor()
cur.execute("select * from emp")

for i in cur:
    print(i)
conn.close()
