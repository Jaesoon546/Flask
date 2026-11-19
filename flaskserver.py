from flask import Flask, request, render_template, jsonify 
import os
import json
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from dao import sungjuk

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
CSRFProtect(app)
# http://127.0.0.1:5000 서비스
# http://127.0.0.1:5000/view/변수이름  
@app.route('/view/<prod_name>')
def view_product(prod_name): # business 로직 
    return 'product name: %s' % prod_name # 문자열을 리턴 
# http://127.0.0.1:5000/info/웹프로그래밍/플라스크
@app.route('/info/<category>/<prod_name>')
def show_prodinfo(category, prod_name):
    return 'product info: %s(%s)' % (prod_name, category)

@app.route("/w3")
def w3():
    return render_template("w3schools.html") #진자를 이용해서 값을 채움

@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap/bootstrap.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/javascript1")
def javascript1():
    return render_template("javascript1.html")


@app.route("/index")
def index():
    return render_template("index.html")

# 순수하게 데이터만 송수신 
@app.route("/ajaxcall")
def ajaxcall():
    return render_template("ajax.html")

# JSON : 자바스크립트 -> 파이썬 파싱 -> JSON:javascript
@app.route("/_add_numbers")
def add_numbers():
    # args는 get 방식으로 데이터를 요청할 떄 파싱되는 위치
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    # {'result:30}
    return jsonify(result=a+b)

@app.route("/sungjuk_call")
def sungjuk_call():
    result = sungjuk.getSungjuk()
    return render_template("sungjuk.html", object_list=result)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True, use_reloader=True)