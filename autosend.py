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

# Define the output list file name here
listfile = 'list.txt'

# Define the extension of the files to be listed
extension = "*.exe"

# Find all files with the extension in this directory
liste = glob.glob("C:\Windows\System32\%(extension)s" % locals())

f = open(listfile, 'w')
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

# login to the email account
yagmail.register(username, password)

print("User registred successfully")

receiverData = config['reciever_mail']
subjectData = config['subject']
contentsData = config['contents']
attachData = listfile

try:
    yag.send(to=receiverData,
             subject=subjectData,
             contents=contentsData,
             attachments=attachData)
    print("Email sent successfully")

# Error example:  Emailaddress "examplemail.com" is not valid according to RFC 2822 standards
except Exception as error:
    print("Error: ", error)
