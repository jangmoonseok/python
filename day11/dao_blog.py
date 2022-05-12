import pymysql
class DaoBlog:
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", password="python", port=3305, database="python", charset="utf8")

        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def myinsert(self,values):
        sql = f"insert into blog values('{values[0]}', '{values[1]}', '{values[2]}', '{values[3]}', '{values[4]}', '{values[5]}')"
        cnt = self.cur.execute(sql)
        return cnt
        
    def __del__(self):
        self.cur.close()
        self.conn.close()
    
if __name__ == '__main__':
    de = DaoBlog()
    cnt = de.myupdate(1, ['5','5','5'])
    print(cnt)
    de.conn.commit()
