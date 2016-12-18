#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
(\d(3)|\d(3)\))?            #area code
(\s|-|\.)?                  #separator
(\d(3))                     #first 3 digs
(\s|-|\.)                   #separator
(\d(4))                     #last 4 digs
(\s*(ext|x|ext.)\s*(\d(2,5))? #extension
)''',re.VERBOSE)

#Phone number begins with optional area code, so the ac code group is followed with a ?
#The ac can be just 3 digs - > \d(3) or 3 digs within parens -> | (\d(3)\)
#Separtor characer can be a space or a hyphen or period. join by pipes
#Rest is simple and straightforward
#Last part is an optional extension made up of any number of spaces followed by ext x or ext.
#then followed by 2 to 5 digs.

# Create email regex.
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+            #username
@                            #@ symbol
[a-zA-Z0-9.-]+               #Domain name
(\.[a-zA-Z]{2,4})            # dot-something
)''',re.VERBOSE)


#Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

#Copy results to the clipboard
if len(matches)>0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.') 
