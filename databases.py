from model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name,email,phone,info):
	"""Add a user to the DB."""
	send_to_email = 'waseem.muneer102@gmail.com'
	message = "TalenTeam! A new challenger approaches! {} sent a request,\n '{}' \n \n \n Phone Number => {} \n \n Personal Email => {} ".format(name, info, phone, email)
	msg = MIMEMultipart()
	msg['From'] = 'talenteambot@gmail.com'
	msg['To'] = send_to_email
	msg['Subject'] = "IMPORTANT from the website"
	# Attach the message to the MIMEMultipart object
	msg.attach(MIMEText(message, 'plain'))
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login('talenteambot@gmail.com', 'teamD3isbest')
	text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send
	server.sendmail('talenteambot@gmail.com', send_to_email, text)
	server.quit()
	motherfking_customer = User(name=name, email=email, phone=phone, Info=info)
	session.add(motherfking_customer)
	session.commit()

def get_user(name):
	"""Find the first user in the DB, by their username."""
	return session.query(User).filter_by(name=name).first()