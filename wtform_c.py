from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired , EqualTo,Length, ValidationError
from model import User
from passlib.hash import pbkdf2_sha256


def check_creditials(form,field):
    username_ent= form.username.data
    password_ent=field.data

    user_object = User.query.filter_by(username=username_ent).first()
    if user_object is None:
        raise ValidationError('invalid creditials')
    elif not pbkdf2_sha256.verify(password_ent, user_object.password):
        raise ValidationError('invalid creditials')

class Registrationform(FlaskForm):
    username= StringField('username_label',validators=[InputRequired(message="This field cannot be empty"),Length(min=4, max=20, message="Size of character must be between 4 and 20")])
    password= PasswordField('pswd_label', validators=[InputRequired(message="This field cannot be empty"),
                                                      Length(min=4, max=20, message="Size of character must be between 4 and 20")])
    
    cnf_pswd= PasswordField('cnf_label',validators=[InputRequired(message="This field cannot be empty"),EqualTo('password',message="password must be same")])

    submit= SubmitField('create')


    # custom validation
    # validate_username ki jagah dusra naam rakhna hai to upar pass karna hoga function
    def validate_username(self,username):   
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError('username exist. select  another')
        

class LoginForm(FlaskForm):
    username= StringField('username_label',validators=[InputRequired(message="This field cannot be empty")])
    password= PasswordField('pswd_label', validators=[InputRequired(message="This field cannot be empty"),check_creditials])

    submit= SubmitField('login')