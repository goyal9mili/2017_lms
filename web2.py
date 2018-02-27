import requests
import urllib2
import datetime
from bs4 import BeautifulSoup
open("output.txt", "w").close() # output.txt is the text file where you want to push the updates.
file = open("output.txt","a")
time = str(datetime.datetime.now())
file.write(time + "\n")
POST_LOGIN_URL="https://lms.iiitb.ac.in/moodle/my/"

REQUEST_URL="https://lms.iiitb.ac.in/moodle/login/index.php"
payload = {
    'username': #Enter your id
	'password': #Enter your password
}
with requests.Session() as session:
	post = session.post(REQUEST_URL, data=payload,verify=False)
	r = session.get(POST_LOGIN_URL,verify = False)
	soup = BeautifulSoup(r.content,"html.parser")
	for t in soup.find_all('div',{'class':'box coursebox'}):
		for i in t.find_all('h2'):
			for j in t.find_all('div',{'class':'collapsibleregion collapsed'}):
				for k in j.find_all('div',{'class':'collapsibleregioncaption'}):
					if j.find_all('div',{'class':'collapsibleregioncaption'}):
						file.write(i.text)
                        			file.write("\n")
                    			else:
                        			file.write("no new updates")
		for j in t.find_all('div',{'class':'collapsibleregion collapsed'}):
			for k in j.find_all('div',{'class':'collapsibleregioncaption'}):
				for s in k.find_all('div',{'class':'collapsibleregioninner'}):
                			for m in s.find_all('div',{'class':'assign overview'}):
                				file.write(m.text)
				file.write (k.text)
                file.write("\n")

# CRONJOB LINE ADDED : " 0 * * * * python /path to file /web2.py"
