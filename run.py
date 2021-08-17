from ruvenweb import app, config


if __name__ == '__main__':
    config.read("ruvenweb/config.ini")
    app.run(host="0.0.0.0", debug=config['APP']['debug'])




