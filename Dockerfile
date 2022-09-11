FROM silverlogic/python3.8
WORKDIR /opt/app
COPY . .
RUN pip install requests flask flask_sqlalchemy flask_wtf flask_login redis flask_bcrypt email_validator

CMD ["python3", "run.py"]
