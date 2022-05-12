from flask import Flask,render_template,request,redirect,jsonify
from day08 import dao_emp
# app = Flask(__name__)
app = Flask(__name__,  static_url_path="")

dao = dao_emp.DaoEmp()

@app.route('/emp')
def emp():
    return render_template('emp.html')

@app.route('/ajaxList')
def ajax():
    emps = dao.myselects()
    return jsonify({'emps': emps})

@app.route('/ajaxDetail')
def ajaxDetail():
    e_id = request.args.get("e_id")
    
    emp = dao.myselect(e_id)
    return jsonify({'emp' : emp})

@app.route('/ajaxAdd', methods=["POST"])
def ajaxAdd():
    data = request.get_json()
    e_id = data['e_id']
    e_name = data['e_name']
    sex = data['sex']
    addr = data['addr']
    cnt = dao.myinsert(e_id, e_name, sex, addr)
    dao.conn.commit()
    
    return jsonify({'cnt' : cnt})

@app.route('/ajaxDelete', methods=["GET"])
def ajaxDelete():
    e_id = request.args.get('e_id')
    cnt = dao.mydelete(e_id)
    dao.conn.commit()
    
    return jsonify({'cnt' : cnt})

@app.route('/ajaxUpdate', methods=["POST"])
def ajaxUpdate():
    data = request.get_json()
    e_id = data['e_id']
    e_name = data['e_name']
    sex = data['sex']
    addr = data['addr']
    values = [e_name, sex, addr]
    cnt = dao.myupdate(e_id, values)
    dao.conn.commit()
    
    return jsonify({'cnt' : cnt})
if __name__ == '__main__':
    app.run(debug=True)