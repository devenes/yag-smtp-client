from config import config
import logging
import yagmail


logging.basicConfig(
    filename=config['log_file'],
    level=config['log_level'])


username = config['sender_mail']
password = config['password']

yag = yagmail.SMTP(username)

yagmail.register(username, password)

print("User registred successfully")

# Get the receiver mail address
receiver = input("Please write the receiver email: ")
# Get the subject of the mail
subs = input("Please write the subject: ")
# Get the contents as a string
cons = input("Please write the contents: ")


receiverData = receiver
subjectData = ("'"+subs+"'")
contentsData = ("'"+cons+"'")


try:
    yag.send(to=receiverData,
             subject=subjectData,
             contents=contentsData)
    print("Email sent successfully")

# Example: Error:  Emailaddress "adsassmail.com" is not valid according to RFC 2822 standards
except Exception as error:
    print("Error: ", error)
