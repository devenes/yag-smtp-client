from config import config
import logging
import yagmail

logging.basicConfig(
    filename=config['log_file'],
    level=config['log_level'])

username = config['user']
password = config['password']
yag = yagmail.SMTP(username)

yagmail.register(username, password)

print("User registred successfully")

reciver = input("Please write the reciver email: ")
subs = input("Please write the subject: ")
cons = input("Please write the contents: ")

reciverData = reciver
subjectData = ("'"+subs+"'")
contentsData = ("'"+cons+"'")

try:
    yag.send(to=reciverData,
             subject=subjectData,
             contents=contentsData)
    print("Email sent successfully")

# Example: Error:  Emailaddress "adsassmail.com" is not valid according to RFC 2822 standards
except Exception as error:
    print("Error: ", error)
