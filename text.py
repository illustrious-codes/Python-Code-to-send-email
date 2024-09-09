import smtplib

sender = "illustriouscodes@gmail.com"
receiver = "Tiaraoluwa80@gmail.com"
password = "nzfubvhlbwzaecjb"
subject = "ILLUSTRIOUS CODE"
body = "I Love You"

message = f""" From: Illustrious {sender}
To: Miya {receiver}
Subject: Texting my Python Code {subject}\n
{body} """

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except: 
    print("Unable to sign in")