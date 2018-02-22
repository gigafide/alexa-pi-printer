#!flask/bin/python

from flask import Flask, request
from escpos.printer import Usb

p = Usb(0x0416, 0x5011)
app = Flask(__name__)

#CREATE 'INDEX' PAGE
@app.route('/')
def index():
	return 'Your Flask server is working!'

#CREATE A "PAGE" CALLED "TWEETS" FOR PRINTING NEW TWEETS
@app.route('/tweet')
def tweet():
	#CAPTURE "GET" DATA FROM IFTTT WEBOOKS
	tweet_raw = request.get_data()

	#CONVERT RAW DATA TO STRING
	tweet_content = str(tweet_raw)

	#DIVIDE DATA INTO SEPERATE LINES
	tweet_split = tweet_content.splitlines()

	#SEPERATE ITEMS BY SEMICOLON AND ADD TO A NEW LIST
	new_tweetlist = []
	for word in tweet_split:
		word = word.split(';')
		new_tweetlist.extend(word)

	#REMOVE FORMATTING MARTKS
	rmv_marks = [s.strip("b'") for s in new_tweetlist]

	#LOOP THROUGH NEW LIST AND PRINT RESULTS
	print("New Tweet From:\n")
	p.text("New Tweet From:\n")

	#LOOP THROUGH NEW LIST AND PRINT RESULTS
	for x in rmv_marks:
		print (x + "\n")
		p.text(x + "\n")

	#RETURN RESULTS
	return(x)

#RUN THE PROGRAM
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
