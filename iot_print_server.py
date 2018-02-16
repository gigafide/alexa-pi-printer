#!flask/bin/python

from flask import Flask, request
from escpos.printer import Usb

p = Usb(0x0416, 0x5011)
app = Flask(__name__)

#CREATE 'INDEX' PAGE
@app.route('/')
def index():
	return 'Your Flask server is working!'

#CREATE 'LIST' PAGE FOR PRINTING SHOPPING LIST
@app.route('/list')
def list():

	#REQUEST DATA FROM WEBHOOKS
	content = request.get_data()

	#CONVERT RAW DATA TO STRING
	str_content = str(content)
	
	#DIVIDE DATA INTO SEPERATE LINES
	str_split = str_content.splitlines()

	#SEPERATE WORDS BY COMMA AND ADD TO A NEW LIST
	newlist = []
	for word in str_split:
		word = word.split(',')
		newlist.extend(word)

	#REMOVE FORMATTING MARKS
	rmv_marks = [s.strip("b'") for s in newlist]

	#PRINT HEADER
	#print("Shopping List\n")
	p.text("Shopping List:\n")

	#ENUMERATE AND PRINT EACH ITEM IN LIST
	r = 1
	for x in rmv_marks:
		#print(str(r) + ". " + x + "\n")
		p.text(str(r) + ". " + x + "\n")
		r += 1

	return 'x'

#CREATE 'TO DO' PAGE FOR PRINTING TO DO LIST
@app.route('/todo')
def list():
	content = request.get_data()
	str_content = str(content)
	str_split = str_content.splitlines()
	newlist = []
	for word in str_split:
		word = word.split(',')
		newlist.extend(word)
	rmv_marks = [s.strip("b'") for s in newlist]
	p.text("To Do List:\n")
	r = 1
	for x in rmv_marks:
		p.text(str(r) + ". " + x + "\n")
		r += 1
	return 'x'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
