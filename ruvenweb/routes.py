from ruvenweb import app
from flask import render_template, redirect, url_for
from ruvenweb.form_for_feedback import RegisterFeedback
from ruvenweb.model import Feedback
from ruvenweb import db


@app.route("/")
def homepage():
    return render_template('base.html')


@app.route("/hobbies")
def hobbies():
    return render_template('hobbies.html')


@app.route("/family")
def family():
    return render_template('family.html')


@app.route("/healthy")
def healthy():
    return "OK"


@app.route("/feedback", methods=['GET', 'POST'])
def feedback():
    db_connection = Feedback.create_connection("ruvenweb/ruvenweb.db")
    Feedback.create_table(db_connection)
    user_comments = Feedback.select_all_tasks(db_connection)
    form = RegisterFeedback()
    if form.validate_on_submit():
        comment = Feedback(name=form.username.data, email=form.email.data, description=form.descreption.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('homepage'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            print(f'There was an error with creating a user: {err_msg}')
    return render_template('feedback.html', form=form, users_comments=user_comments)


@app.route("/workexperience")
def workexperirnce():
    experirnce = [{'years': '2016-2019', 'company': 'Nokia', 'role': 'Networking software engineer'},
                  {'years': '2019-2020', 'company': 'Trax', 'role': 'DevOps engineer'},
                  {'years': '2020-2021', 'company': 'Nokia', 'role': 'Infra engineer'}]
    return render_template('workexperience.html', experirnces=experirnce)


@app.route("/eduction")
def eduction():
    return render_template('eduction.html')




