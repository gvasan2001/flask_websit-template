from flask import *

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/admin_login_page')
def adminLoginPage():
    return render_template("adminLogin.html")

@app.route('/admin_login', methods=['POST','GET'])
def adminLogin():
    uname=request.form['box1']
    password=request.form['box2']
    if uname=="admin" and password== "admin":
        return render_template("adminHome.html")
    else:
        return render_template('adminHome.html',data="your Username or password is worng")



# medial men part
@app.route('/medial_login_page')
def medialmen_login_page():
    return render_template('medialmen_login_page.html')

@app.route('/medial_login')
def medial():
    name=request.form['box1']
    password=request.form['box2']
    print(name,password)


# user part
@app.route('/user_loginPage')
def user_loginPage():
    return render_template('user_login.html')

@app.route("/user_login",methods=['POST','GET'])
def user_login():
    name=request.form['box1']
    password=request.form['box2']
    return "null"

@app.route('/registerPage')
def registerPage():
    return render_template('user_registerPage.html')

@app.route('/user_register' ,methods=['post','get'])
def user_register():
    id=""
    a=request.form['box1']
    b = request.form['box2']
    c = request.form['box3']
    d = request.form['box4']
    e = request.form['box5']
    f = request.form['box6']
    g = request.form['box7']
    h = request.form['box8']
    status=""
    aa.register("INSERT INTO user_detials values ('"+id+"','"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"','"+status+"')")
    return redirect('registerPage')

if __name__=="__main__":
    app.run(debug=True)
