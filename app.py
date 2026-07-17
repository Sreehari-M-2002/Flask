from flask import Flask, render_template, request,url_for,redirect
from models import db,Student


app = Flask(__name__)
#above are configuration setups

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

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

@app.route('/add_students', methods=['GET','POST'])
def Add_students():
    
    if request.method=='POST':

        name=request.form.get('name')
        desc = request.form.get('desc')

        # print(name)
        # print(desc)

        student= Student(
            name=name,
            desc=desc
        )

        db.session.add(student)
        db.session.commit('desc')
        return redirect(url_for('Add_Students'))
    
    get_student = Student.query.all()
    return render_template('students_sheet.html',students=get_student)


#below are configuration setups
if __name__ == '__main__':
    app.run(debug=True)