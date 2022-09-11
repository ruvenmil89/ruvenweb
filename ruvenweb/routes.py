from ruvenweb import app, config
import json
import requests
from flask_login import (
    UserMixin, login_user, LoginManager, login_required, logout_user, current_user
)
from flask import (
    render_template,
    make_response,
    g,
    redirect,
    session,
    url_for,
    flash,
    request
)
from flask_wtf import CSRFProtect
from ruvenweb.form_for_feedback import RegisterFeedback
from ruvenweb.model import Feedback
from ruvenweb.UsersLogin import UserLogin, RegisterFormLogin, LoginForm, UpdatePassword
from ruvenweb import db
from redis import Redis as redis
from flask_bcrypt import Bcrypt

config.read("ruvenweb/config.ini")
efk_url = config['TOOLS']['EFK_URL']
if config['APP']['ENVIRONMENT'] == 'kubernetes':
  redis_url = config['TOOLS']['REDIS_URL'] + "." + config['TOOLS']['REDIS_NAMESPACE'] + ".svc.cluster.local"
else:
  redis_url = config['TOOLS']['REDIS_URL']
csrf = CSRFProtect()
csrf.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
bcrypt = Bcrypt(app)
r = redis(host="{}".format(redis_url), port=6379)


def rateLimit(userid) -> bool:
    send_log(userid)
    r.setnx(userid, 3)
    r.expire(userid, 10)
    if int(r.get(userid)) > 0:
        r.decr(userid)
        return True
    return False


@login_manager.user_loader
def load_user(user_id):
    return UserLogin.query.get(int(user_id))


def send_log(userid):
    data = {'user': "Just {} enter".format(userid)}
    data_json = json.dumps(data)
    #r = requests.get('http://{}:9880/ratelimit.log'.format(efk_url), json=data)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserLogin.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Login successful')
                return redirect(url_for('homepage'))

    return render_template("login.html", form=form)


@app.route("/", methods=["GET", "POST"])
@login_required
def homepage():
    if not rateLimit(request.remote_addr):
        return redirect(url_for('ratelimit'))
    return render_template('base.html')


@app.route("/ratelimit")
def ratelimit():
    return render_template('ratelimit.html')


@app.route("/hobbies")
def hobbies():
    return render_template('hobbies.html')


@app.route("/family")
@login_required
def family():
    return render_template('family.html')


@app.route("/healthy")
def healthy():
    return "OK"


@app.route("/feedback", methods=['GET', 'POST'])
def feedback():
    user_comments = Feedback.query.all()
    form = RegisterFeedback()
    if form.validate_on_submit():
        comment = Feedback(name=form.username.data, email=form.email.data, description=form.descreption.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('feedback'))
    return render_template('feedback.html', form=form, users_comments=user_comments)


@app.route("/workexperience")
def workexperirnce():
    experirnce = [{'years': '2016-2019', 'company': 'Ben Gurion University', 'role': 'teaching assistant: lectures in the course Network Function Virtualization and supervisor in the communication network lab'},
                  {'years': '2016-2019', 'company': 'Nokia', 'role': 'Software engineer  Development and support of an OpenStack based infrastructure software '
                                                                     'responsible for development of an upgrade procedure for CBIS (one of the most complex procedures in CBIS) '
                                                                     'Design and development of the "all in one" OpenStack TripleO product '
                                                                     'Onboarding NOKIA’s VNF’s on top on CBIS openstack platform '
                                                                     'Participating in the design of NOKIA’s Mobile Edge platform CloudBand CTO group: research intern. '
                                                                     'Research on Virtualization technologies, NFV, OpenStack platform, Containers, Kubernetes, and hardware acceleration'},
                  {'years': '2019-2020', 'company': 'Trax', 'role': 'DevOps engineer, Developing the CI/CD of Trax by using Jenkins'
                                                                    'Build and develop complex procedures, for example, project creation which means creation many cloud resources without DevOps intervention'
                                                                    'Responsible for the cloud billing – I developed ETL of tagging the resources in AWS and GCP, collecting the data (by using Athena and Big query), save the data in RDS and present the data in Tableau.'},
                  {'years': '2020-till now', 'company': 'Nokia', 'role': 'Infra engineer, In this role I act as team leader as well as a technical contributor.'
                                                                     ' I have split huge code to microservices and created Helm charts to deploy the applications.'
                                                                     ' I built automation to install the product in CI/CD'
                                                                     'I was working on the product integration and deployment over IPv6 networking '
                                                                         'I helped to deploy the product in Nokia\'s customers ( including Verizon and Rakuten )'}]
    return render_template('workexperience.html', experirnces=experirnce)


@app.route("/eduction")
def eduction():
    return render_template('eduction.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    current_user.username = current_user.username[0].upper() + current_user.username[1:]
    form = UpdatePassword()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = UserLogin.query.filter_by(username=current_user.username).first()
            if user:
                if bcrypt.check_password_hash(user.password, form.oldpassword.data):
                    user.password = bcrypt.generate_password_hash(form.newpassword.data)
                    db.session.commit()
                    flash('Password updated!')
    return render_template('profile.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterFormLogin()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(password=form.password.data)
        new_user = UserLogin(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}')
    return render_template('register.html', form=form)


