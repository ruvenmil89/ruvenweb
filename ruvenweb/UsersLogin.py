from flask_login import UserMixin
from flask_wtf import FlaskForm

from ruvenweb import db
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired,Length,ValidationError


class UserLogin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False,unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterFormLogin(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existusername = UserLogin.query.filter_by(username=username.data).first()
        if existusername:
            raise ValidationError("The username already exists")


class UpdatePassword(FlaskForm):
    oldpassword = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "old Password"})
    newpassword = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "new Password"})
    submit = SubmitField("Update password")


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

