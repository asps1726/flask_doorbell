from flask import Flask,request,render_template
import os
from datetime import datetime
import winsound 

music = '夜に駆ける.wav'
host = "0.0.0.0"


today = datetime.now()

app = Flask(__name__)

@app.route('/',methods=['POST', 'GET'])
def index():
	if request.method =='POST':
		if request.values['send']=='送出' and request.form['user'] != "":
			data = request.form['user']
			
			with open('log.txt', 'a') as f:
				f.write("時間：")
				f.write(today.strftime("%m/%d/%Y %H:%M:%S") + "\t")
				f.write("訪客:")
				f.write(data + "\t")
				f.write("\n")
			#print(data)
			#print(os.getcwd())

			os.system(music)

			return render_template('index.html',name=request.values['user'])
	return render_template('index.html',name="")


if __name__ == '__main__':
		app.run(host = host,debug=True, port= 1726)
