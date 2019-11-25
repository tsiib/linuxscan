
from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'bess.testin@gmail.com',
    "MAIL_PASSWORD": os.environ['bess.testing123']
}

app.config.update(mail_settings)
mail = Mail(app)

