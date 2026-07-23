from flask import Flask, render_template, request,url_for,redirect, session
from models import db,Student, User
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistartionForm


app = Flask(__name__)
#above are configuration setups

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SECRET_KEY'] = 'authenticationkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


#<--------  _____             _____          _____  __   __        ------------->
#<--------  |__   |      /\   |____  |/ ___  |__   |  | |__| |\/|  ------------->
#<--------  |     |____ /--\  _____| |\      |     |__| | \  |  |  ------------->
#<--------                                                         ------------->

 
@app.route('/register', methods =['GET', 'POST'])
def register():

    form = RegistartionForm()
    if form.validate_on_submit():
        print(form.username.data)
        return redirect(url_for('success'))

    return render_template('register.html', form=form)

@app.route('/success')
def succes():
    return render_template('success.html')





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

#<-----------------SignUp Page-------------------------->

@app.route('/signup', methods=['GET', 'POST'])
def Register():

    if request.method == 'POST':

        fname = request.form.get('fname')
        lname = request.form.get('lname')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        hashed_password = generate_password_hash(password)

        user = User(
            fname=fname,
            lname=lname,
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('Login'))

    return render_template('signup.html')

#<------------- LogIN Page------------->

@app.route('/login', methods=['GET', 'POST'])
def Login():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password,password):
            
            session['user_id'] = user.id

            return redirect(url_for('Add_students'))

    return render_template('login.html')


#<-------------Log Out ------------->


@app.route('/logout')
def logout():
    session.pop('user_id',None)
    return redirect(url_for('Login'))

#@login_required = login_url('login')




#<-----------------ADD STUDENTS----------------->


@app.route('/add_students', methods=['GET', 'POST'])
def Add_students():

    if 'user_id' not in session:
        return redirect(url_for('Login'))


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







#<--------below are configuration setups-------->

if __name__ == '__main__':
    app.run(debug=True)
