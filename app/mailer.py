from threading import Thread

from flask import render_template
from flask_mail import Message

from app import app, mail
from config import ADMINS, MAIL_SERVER


class Mailer:
    """
    Some helper for mail sending.
    """
    @staticmethod
    def send_async_email(msg):
        with app.app_context():
            mail.send(msg)

    def send_email(self, subject, sender, recipients, text_body, html_body):
        msg = Message(subject, sender=sender, recipients=recipients)
        msg.body = text_body
        msg.html = html_body
        thr = Thread(target=self.send_async_email, args=[msg])
        thr.start()

    def send_to_admin(self, subject, text_body, html_body):
        msg = Message(subject, sender=ADMINS[0], recipients=ADMINS)
        msg.body = text_body
        msg.html = html_body
        thr = Thread(target=self.send_async_email, args=[msg])
        thr.start()

    @staticmethod
    def new_tle_notify(data):
        msg = Message("New TLE notification", sender='notify@' + MAIL_SERVER, recipients=ADMINS)
        msg.body = render_template("new_tle.txt", data=data)
        thr = Thread(args=[msg])
        thr.start()

    @staticmethod
    def tle_provider_fail_notify():
        msg = Message("TLE provider fail", sender='notify@' + MAIL_SERVER, recipients=ADMINS)
        msg.body = render_template("tle_fail.txt")
        thr = Thread(args=[msg])
        thr.start()
