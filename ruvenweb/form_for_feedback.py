from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Email, DataRequired


class RegisterFeedback(FlaskForm):
    username = StringField(label='User name:', validators=[Length(min=1)])
    email = StringField(label='Email address:')
    descreption = StringField(label='Comment:', validators=[DataRequired()])
    submit = SubmitField(label='Send your comment')


