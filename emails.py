import smtplib
import time
import imaplib
import email
import base64
import logging
import logging.config
from datetime import date
from configparser import ConfigParser


class Emails:

    def __init__(self):
        today = date.today()
        date_ = str(today.year) + str(today.month) + str(today.day)
        self.configurate = ConfigParser()
        self.configurate.read('config/configEmails.init')
        smtp_server = self.configurate.get('server', 'SMTP_SERVER')
        smtp_port = self.configurate.get('server', 'SMTP_PORT')
        file_log = self.configurate.get('server', 'LOG')
        log_log = 'logs/' + file_log.replace('$fecha', date_)
        logging.config.fileConfig('config/configLogEmail.ini', disable_existing_loggers=False, defaults={'logfilename': log_log})
        self.log = logging.getLogger('emailLog')
        self.log.info('Inicia la clase email')
        self.mail = imaplib.IMAP4_SSL(smtp_server, int(smtp_port))
        self.log.info('Se crea la variable de session para el mail')

    def open_connect(self, process):
        email_user = self.configurate.get(str(process), 'FROM_EMAIL')
        email_pass = self.configurate.get(str(process), 'FROM_PWD')
        self.log.info('Usuario -> ' + email_user)
        self.log.info('Pass -> ' + email_pass)
        self.mail.login(email_user, email_pass)

    def get_logger(self):
        return self.log

    def get_messages(self):
        self.mail.select('Inbox')
        return self.mail.search(None, 'ALL')

    def get_mail(self):
        return self.mail

    def close_connect(self):
        self.mail.close()


if __name__ == '__main__':
    correo = Emails()
    #log_ = correo.get_logger()
    correo.open_connect("proceso_sm")
    mails = correo.get_mail()
    correos = correo.get_messages()
    correo.close_connect()


