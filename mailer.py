# -*- coding: utf-8 -*-
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


class Mailer:
  def __init__(self):
    self.message = open('message.txt', "rt").read()
    body = open('receivers.txt', "rt").read()
    self.receivers = [item.rstrip() for item in body]
    self.password = ""
    self.sender_email = ""
    self.port = 587 # or 465 
    self.server = "smtp.gmail.com"

  def send_email(self):
      """
        Send html or text email.
      """
      if self.port==465:
          smtp_server = smtplib.SMTP_SSL(self.server, self.port)
      elif self.port==587:
          smtp_server = smtplib.SMTP(self.server, self.port)
          smtp_server.ehlo()
          smtp_server.starttls()
      smtp_server.login(self.sender_email, self.password)
      types = 'plain'
      regex_html = '(?i)<\/?\w+((\s+\w+(\s*=\s*(?:".*?"|\'.*?\'|[^\'">\s]+))?)+\s*|\s*)\/?>'
      if re.match(regex_html, self.message):
          types = 'html'
      msg = MIMEMultipart('alternative')
      msg['Subject'] = Header(subject, 'utf-8')
      msg.attach(MIMEText(self.message, types, 'utf-8'))
      for user in self.receivers:
        smtp_server.sendmail(sender_email, user, msg.as_string())
      smtp_server.close()


receivers = open('receivers.txt', "rt").readlines()
receivers = [item.rstrip() for item in receivers]
print(receivers)