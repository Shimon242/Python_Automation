import re

#passwordEx = re.compile(r''' (
#^(?=.*[A-Z].*[A-Z])        Ensure string has two uppercase letters.
#(?=.*[!@#$&*])            Ensure string has one special case letter.
#(?=.*[0-9].*[0-9])        Ensure string has two digits.
#(?=.*[a-z].*[a-z].*[a-z]) Ensure string has three lowercase letters.
#.{8}                      Ensure string is of length 8.
#$                         End anchor.

strong_pwd_regex = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')

password = input('Please enter password')

if bool(strong_pwd_regex.search(password)) == False:
	print("Weak password")
else:
	print("Strong password")
