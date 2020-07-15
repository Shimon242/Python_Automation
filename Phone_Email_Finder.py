import re, pyperclip

# Ensure you have the text you want in clipboard already!!!

# 415-555-0000, 555-0000, (415) 555-0000 ext 12345, ext. 12345, x12345
phoneRegex = re.compile(r'''
(	
((\d\d\d)|(\(\d\d\d\)))? #area code optional
(\s|-) #first separator
\d\d\d #first 3 digits
- #separator
\d\d\d\d # last 4 digits
(((ext(\.)?\s)|x) # extension word-part
(\d{2,5}))? #extension number-part
)
''', re.VERBOSE)

# Rigex for email addresses

emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+ # name part
@ # @ symbol
[a-zA-Z0-9_.+]+ # domain name part

''', re.VERBOSE)

# Get text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for PhoneNumber in extractedPhone:
	allPhoneNumbers.append(PhoneNumber[0])

# Copy the extracted phone numbers to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)

pyperclip.copy(results)

print(results)
