# send mail to me through python script
# keep cc to other two if sivani is writing script she will keep radha and naga in cc

# Simple Mail Transfer Protocol (SMTP) is used to send a mail
import smtplib

from_mail = 'grandheraj68@gmail.com'
password = 'vezircpgrcrhbaqb'

to = ['vibha.rawan@neosoftmail.com']
cc = ['lakshmi73862@gmail.com', 'radha.maredi@gmail.com']
bcc = ['arun.nadar@neosoftmail.com', 'rohan.dhere@neosoftmail.com']

subject = "Generated mail using Python"
body = "Hi! this mail is generated using python code by Sivani Raj"

message = """\
From: %s
To: %s
Subject: %s
cc: %s
%s
""" % (from_mail, ", ".join(to), subject, ", ".join(cc),  body)

# puts the connection to the SMTP server into SSL (Secure Socket Layer) mode.
# smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# have to pass the server address and port number
server = smtplib.SMTP('smtp.gmail.com', 587)

# puts the connection to the SMTP server into TLS mode.
server.starttls()

server.login(from_mail, password)
server.sendmail(from_mail, to + cc + bcc, message)

# Closing connection
server.close()
print("Email is sent Successfully!")
