from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import Length, Email, DataRequired


class RegisterFeedback(FlaskForm):
    username = StringField(label='User name:', validators=[Length(min=1)])
    email = EmailField(label='Email address:', validators=[DataRequired(), Email()])
    descreption = StringField(label='Comment:', validators=[DataRequired()])
    submit = SubmitField(label='Send your comment')


