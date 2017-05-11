import logging

import flask
# import requests


app = flask.Flask(__name__)
log = logging.getLogger()
file_logger = logging.FileHandler('/var/log/spa.log')
log.addHandler(file_logger)
stdout_logger = logging.StreamHandler()
log.addHandler(stdout_logger)
log.setLevel(logging.DEBUG)


@app.route('/', methods=['GET', 'POST'])
def home():
    if flask.request.method == 'POST':
        log.debug("You've added {} to log entry!".format(
            flask.request.form['first']))
        return flask.redirect(flask.url_for('home'))
    return flask.render_template('index.html')


@app.route('/logs/', methods=['GET'])
def logs():
    with open('/var/log/spa.log', 'r') as log_file:
        return ''.join(log_file.readlines())


if __name__ == '__main__':
   app.run(debug=True)
