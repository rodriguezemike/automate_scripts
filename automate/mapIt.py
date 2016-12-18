#! python3 
# mapIt.py -> Launches a map in the broswer using an address from the command line or clipboard.  
import webbrowser, sys
if len(sys.argv) > 1 :
    #Get Address from cmd line
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
