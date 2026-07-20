from flask import Flask, render_template, request,url_for,redirect
from models import db,Student


app = Flask(__name__)
#above are configuration setups

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# <-----------HOME---------->


@app.route('/')  #end point
def home():      #function
    return render_template('home.html')


#<---------------USER---------->

@app.route('/user')
def user():

    name = 'sreehari'
    position = 'student'
    marks = 60
    return render_template('user.html', name=name, position=position, marks=marks)

#<------------LOOP--------------->

@app.route('/loop')
def loop():
    subjects = ['flask', 'flaskapi', 'django']

    return render_template('loop.html',subjects=subjects)


#<-----------------ADD STUDENTS----------------->


@app.route('/add_students', methods=['GET', 'POST'])
def Add_students():

    if request.method == 'POST':

        name = request.form.get('name')
        desc = request.form.get('desc')

        student = Student(
            name=name,
            desc=desc
        )

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('Add_students'))

    get_student = Student.query.all()
    return render_template('students_sheet.html', students=get_student)

#<---------------------DELETE STUDENTS---------------->

@app.route('/delete_students/<int:id>/')
def remove_student(id):

    student = Student.query.get(id)

    db.session.delete(student)
    db.session.commit()

    return redirect(url_for('Add_students'))

#<--------------UPDATE------------->

@app.route('/alter_student/<int:id>/', methods=['GET', 'POST'])
def update_student(id):

    student = Student.query.get(id)

    if request.method == 'POST':
        student.name = request.form.get('name')
        student.desc = request.form.get('desc')
        db.session.commit()
        return redirect(url_for('Add_students'))

    return render_template('update.html', student=student)

#<---------- Single student search -------->

@app.route('/full_detail/<int:id>/')
def full_detail(id):

    student = Student.query.get(id)
    return render_template('full_detail.html',student=student)

#<------------------------------------------->

#below are configuration setups

if __name__ == '__main__':
    app.run(debug=True)