from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # return "Hello"
    return render_template('register.html')

@app.route('/submit' , methods=['POST'])
def submitHandle():
    name = request.form['username']
    email = request.form['email']
    mobile = request.form['mobile']
    return render_template('afterRegister.html' , userName=name , userEmail = email , userMobile = mobile )


if __name__ == "__main__":
    app.run(debug=True)