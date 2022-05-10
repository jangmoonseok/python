from flask import Flask,render_template,request,redirect,jsonify
from day08 import dao_emp
app = Flask(__name__)

dao = dao_emp.DaoEmp()

@app.route('/emp')
def emp():
    return render_template('emp.html')

@app.route('/ajaxList')
def ajax():
    emps = dao.myselects()
    return jsonify({'emps': emps})

if __name__ == '__main__':
    app.run(debug=True)