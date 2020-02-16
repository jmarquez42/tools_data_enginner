import smtplib
import time
import imaplib
import email
import base64
import logging
from configparser import ConfigParser

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("Log")

class Emails:

    def __init__(self):
        log.info('Inicia la clase email')
        self.configurate = ConfigParser()
        self.configurate.read('config/config.init')
        smtp_server = self.configurate.get('server', 'SMTP_SERVER')
        smtp_port = self.configurate.get('server', 'SMTP_PORT')
        self.mail = imaplib.IMAP4_SSL(smtp_server, int(smtp_port))
        log.info('Se crea la variable de session para el mail')

    def open_connect(self, process):
        email_user = self.configurate.get(str(process), 'FROM_EMAIL')
        email_pass = self.configurate.get(str(process), 'FROM_PWD')
        log.info('Usuario -> ' + email_user)
        log.info('Usuario -> ' + email_pass)
        self.mail.login(email_user, email_pass)

    def get_messages(self):
        self.mail.select('Inbox')
        return self.mail.search(None, 'ALL')

    def close_connect(self):
        self.mail.close()


if __name__ == '__main__':
    correo = Emails()
    correo.open_connect("proceso_sm")
    correos = correo.get_messages()
    correo.close_connect()


