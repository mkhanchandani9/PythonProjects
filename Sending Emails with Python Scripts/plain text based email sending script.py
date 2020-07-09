import pandas as pd
import smtplib

SenderAddress = "x@gmail.com"
password = "password"

e = pd.read_excel(r"C:\Users\Manisha\Documents\Email.xlsx")
emails = e['Emails'].values

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "Hello this is a email from python"
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()