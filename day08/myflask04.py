from flask import Flask,render_template,request,redirect
from day08 import dao_emp
app = Flask(__name__)

dao = dao_emp.DaoEmp()

@app.route('/list')
def list():
    rows = dao.myselects()
    return render_template('list.html',rows = rows)

@app.route('/list/add', methods=['GET'])
def list_add():
    return render_template('add.html')

@app.route('/list/add', methods=['POST'])
def add():
    e_id = request.form['eid']
    e_name = request.form['ename']
    sex = request.form['sex']
    addr = request.form['addr']
    cnt = dao.myinsert(e_id, e_name, sex, addr)
    dao.conn.commit()
    return render_template('add_act.html', cnt = cnt)

@app.route('/list/update', methods=['GET'])
def list_update():
    e_id = request.args.get('eid')
    data = dao.myselect(e_id);
    return render_template('update.html', data = data)

@app.route('/list/update', methods=['POST'])
def update():
    e_id = request.args.get('eid')
    values = [request.form['ename'], request.form['sex'], request.form['addr']]
    cnt = dao.myupdate(e_id, values)
    dao.conn.commit()
    return render_template('update_act.html', cnt = cnt)

@app.route('/list/delete', methods=['GET'])
def delete():
    
    e_id = request.args.get('eid')
    cnt = dao.mydelete(e_id)
    dao.conn.commit()
    return render_template('delete.html', cnt = cnt)

if __name__ == '__main__':
    app.run(debug=True)