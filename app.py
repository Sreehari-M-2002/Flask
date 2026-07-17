from flask import Flask, render_template
app = Flask(__name__)
#above are configuration setups

@app.route('/')  #end point
def home():      #function
    return render_template('home.html')

@app.route('/user')
def user():

    name = 'sreehari'
    position = 'student'
    marks = 60
    return render_template('user.html', name=name, position=position, marks=marks)

@app.route('/loop')
def loop():
    subjects = ['flask', 'flaskapi', 'django']

    return render_template('loop.html',subjects=subjects)


#below are configuration setups
if __name__ == '__main__':
    app.run(debug=True)