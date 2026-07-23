from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class RegistartionForm(FlaskForm):
    username = StringField('username', validators = [DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('password', validators = [DataRequired(), Length(min=6)])
    submit = SubmitField('Register')
