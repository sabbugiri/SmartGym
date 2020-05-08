import smtplib


def send_email():

	gmail_user = 'corona.ncit12@gmail.com'
	gmail_password = 'Corona98'
	sent_from = gmail_user
	to = 'sabbugiri50@gmail.com'


	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com',465)
		server.ehlo()
		print('Connected to server')
		server.login(gmail_user, gmail_password)
		print('Logged in successfully!!')
		content = email_content(sent_from, to)
		server.sendmail(sent_from,to,content )
		print('Email sent successfully')
		
	except:
		print('Something went wrong...')





def email_content(sent_from, to):
	subject = 'BLALALALA'
	body = "hdlajdljfj"

	email_text = """\
	From : %s	
	To : %s
	Subject : %s
	%s
	"""%(sent_from,"," .join(to), subject, body)

	return email_text		



send_email()	


