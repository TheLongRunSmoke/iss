from flask_mail import Message
from app import app,mail
from config import ADMINS, MAIL_SERVER
from flask import render_template
from threading import Thread

class Mailer():

    def send_async_email(msg):
        with app.app_context():
            mail.send(msg)

    def send_email(subject, sender, recipients, text_body, html_body):
        msg = Message(subject, sender = sender, recipients = recipients)
        msg.body = text_body
        msg.html = html_body
        thr = Thread(target = send_async_email, args = [msg])
        thr.start()

    def send_to_admin(subject, text_body, html_body):
        msg = Message(subject, sender = ADMINS[0], recipients = ADMINS)
        msg.body = text_body
        msg.html = html_body
        thr = Thread(target = send_async_email, args = [msg])
        thr.start()

    def newTleNotification(data):
       msg = Message("New TLE notification", sender = 'notify@'+ MAIL_SERVER, recipients = ADMINS)
       msg.body = render_template("new_tle.txt", data=data)
       thr = Thread(target = Mailer.send_async_email, args = [msg])
       thr.start()

    def tleProviderFail():
       msg = Message("TLE provider fail", sender = 'notify@'+ MAIL_SERVER, recipients = ADMINS)
       msg.body = render_template("tle_fail.txt")
       thr = Thread(target = Mailer.send_async_email, args = [msg])
       thr.start()
