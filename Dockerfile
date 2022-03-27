FROM ubuntu
WORKDIR /opt/app
COPY . .
RUN apt update;apt install software-properties-common -y; add-apt-repository ppa:deadsnakes/ppa;apt update;apt install python3.8 -y;
RUN apt-get install  python3-pip -y; pip install flask flask_sqlalchemy flask_wtf flask_login redis flask_bcrypt email_validator

CMD ["python3", "run.py"]