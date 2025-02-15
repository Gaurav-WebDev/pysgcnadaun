from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    # return "This is Home Page : Flask"
    return render_template('index.html')

@app.route('/about')
def about():
    return "This is About Page"

@app.route('/user')
def user():
    name = "Mohit"
    return render_template('userInfo.html' , user=name)



if __name__ == '__main__':
    app.run(debug=True)