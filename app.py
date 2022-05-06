from config import config
import logging
import yagmail
import glob
import os


logging.basicConfig(
    filename=config['log_file'],
    level=config['log_level'])

# Directory where list will be saved
os.chdir(r"C:\Users\AE\Desktop")

# Define the extension of the files to be sent
extension = "*.exe"

# Find all files with the extension in this directory
liste = glob.glob("C:\Windows\System32\%(extension)s" % locals())

f = open('list.txt', 'w')
for x in liste:
    # write files' path to the file
    f.write(x + '\n')
    # write files' name to the file
    string_bol = x.split("\\", 3)
    # Write to console
    print(string_bol[3])
    # Get the files' name
    dosya_isim = string_bol[3]
    f.write(dosya_isim)
    f.write('\n')

username = config['sender_mail']
password = config['password']
yag = yagmail.SMTP(username)

yagmail.register(username, password)

print("User registred successfully")

receiver = input("Please write the receiver email: ")
subs = input("Please write the subject: ")
cons = input("Please write the contents: ")
attach = 'list.txt'

receiverData = receiver
subjectData = ("'"+subs+"'")
contentsData = ("'"+cons+"'")
attachData = attach

try:
    yag.send(to=receiverData,
             subject=subjectData,
             contents=contentsData,
             attachments=attachData)
    print("Email sent successfully")

# Example: Error:  Emailaddress "adsassmail.com" is not valid according to RFC 2822 standards
except Exception as error:
    print("Error: ", error)
