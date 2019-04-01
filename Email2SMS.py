#importing imaplib for logining in email account

import imaplib

#importing mailparser for extracting information(sender's email etc) from raw mail
import mailparser

#importing time for run a process in every 10 seconds,10 minutes etc
import time

import email
#importing datetime for geting today's date 
import datetime

#importing twilio for connecting to twilio account and sending messege
from twilio.rest import Client

def get_emails():

	#host url like imap.gmail.com
	host = ""

	#email address
	emaill = ''

	#email password
	password = ''

	#connecting to host
	imap = imaplib.IMAP4_SSL(host,993)

	#login in email account
	imap.login(emaill,password)

	#selecting inbox folder in email account
	imap.select("Inbox")

	#enter customized date from which date to which date you want emails on sms
	date=(datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y")

	#geting all the unseen messages from the provided date
	tmp, data = imap.search(None, ('UNSEEN'), '(SENTSINCE {0})'.format(date))
	
	#now iterate over all the unread messages	
	for num in data[0].split():
		tmp,data = imap.fetch(num,"(RFC822)")
		print("MEssege : {0}\n",format(num))
		raw = data[0][1].decode('utf-8')
		mail = mailparser.parse_from_string(raw)
		print(mail.from_)	

		# Your Account Sid and Auth Token from twilio.com/console
		# DANGER! This is insecure. See http://twil.io/secure
		#your twilio account_sid
		#your twilio auth_token 		
		account_sid = ''
		auth_token = ''
		client = Client(account_sid, auth_token)

		message = client.messages.create(
				#sender mobile no
                              from_='+19999999999',
				
                              body=mail.from_,
				#recievers mobile no
                              to='+919999999999'
                          )
		print(message.sid)
	
		break

while True:
	get_emails()
	time.sleep(20)
