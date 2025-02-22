from flask import Flask , render_template , request , redirect , url_for
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# ==> MYSQL Config
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "flaskapp"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
bcrypt = Bcrypt(app)


# ==> Routes
@app.route("/")
def showWelcome():
    return render_template("welcome.html")

@app.route("/signup")
def showSignup():
    return render_template("signup.html")

@app.route("/login")
def showLogin():
    return render_template("login.html")


@app.route("/signupHandle" , methods=['post'])
def signupHandle():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    hashPassword = bcrypt.generate_password_hash(password).decode("utf-8")

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(name , email ,password) VALUES(%s , %s , %s)" , (name , email , hashPassword) )
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('showLogin'))


@app.route('/loginHandle' , methods=['post'])
def loginHandle():
    email = request.form['email']
    password = request.form['password']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s" , (email , ))
    user = cur.fetchone()
    # return user['password']

    if user and bcrypt.check_password_hash(user['password'] ,password):
        return "Login Done"
    else :
        return "Login Failed"



if __name__== "__main__":
    app.run(debug=True)