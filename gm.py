import smtplib
import sys
s = smtplib.SMTP('smtp.gmail.com', 587)
#receiver mail Id
receiver=sys.argv[1]
#Message to be sent
message=sys.argv[2]
s.starttls()
s.login("YOUR_GMAIL_ID","YOUR_GMAIL_PASSWORD")
s.sendmail("YOUR_GMAIL_ID",receiver, message) 
s.quit() 
