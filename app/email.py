from flask_mail import Message
from flask import render_template
from app import mail
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)

sender_email = '.....@gmail.com'
subject_pref = 'Title:'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'projectsmoringa@gmail.com'
app.config['MAIL_PASSWORD'] = 'psw'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False