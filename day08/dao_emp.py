import pymysql
class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", password="python", port=3305, database="python", charset="utf8")

        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def myselects(self):
        sql = "select e_id, e_name, sex, addr from emp"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows
    
    def myselect(self,e_id):
        sql = f"select e_id, e_name, sex, addr from emp where e_id = '{e_id}'"
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        return rows[0]
    
    def myinsert(self,e_id,e_name,sex,addr):
        sql = f"insert into emp values('{e_id}', '{e_name}', '{sex}', '{addr}')"
        cnt = self.cur.execute(sql)
        return cnt
    
    def myupdate(self,e_id,values):
        sql = f"""
                update emp set 
                    e_name = '{values[0]}',
                    sex = '{values[1]}',
                    addr = '{values[2]}'
                 where e_id = '{e_id}'
             """
        cnt = self.cur.execute(sql)
        return cnt
    
    def mydelete(self,e_id):
        sql = f"delete from emp where e_id = '{e_id}'"
        cnt = self.cur.execute(sql)
        return cnt
        
    def __del__(self):
        self.cur.close()
        self.conn.close()
    
if __name__ == '__main__':
    de = DaoEmp()
    cnt = de.myupdate(1, ['5','5','5'])
    print(cnt)
    de.conn.commit()
