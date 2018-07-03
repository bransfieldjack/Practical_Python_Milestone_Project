import os 
import json
import copy
from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.secret_key = "secret"


"""
Reusable function for opening a file and writing to it
"""
def write_file(filename, message):
	with open (filename, 'a') as file:
		file.writelines(message + "\n")



"""
Reusable function for adding text to the messages.txt file
"""



@app.route("/", methods = ["GET", "POST"])
def index():
	"""
	Welcome page, add username. 
	"""
	if request.method == "POST":
		write_file("files/users.txt", request.form["username"])
		return redirect("riddle")
	return render_template("index.html")


@app.route("/riddle", methods = ["GET","POST"])
def riddle():
	#Load the json file containing the riddles
	riddles = []
	with open("data/riddles.json", "r") as riddle_data:
		riddles = json.load(riddle_data)	
		#Set the index to 0 to display the first riddle in the list first
		index = 0
		
		if request.method == "POST":
			index = int(request.form["index"])	#Specify index to be an integer not a string or else will return a type error
			user_answer = request.form["answer"].lower()
			if riddles[index]["answer"] == user_answer:
				index += 1
			else:
				write_file("files/incorrect_answers.json", user_answer)
			
		if request.method == "POST":
			if user_answer == "palmtree" and index >= 7:
				return render_template("game_over.html")
			
	return render_template("riddles.html", riddle_question = riddles, index = index)
	
	
@app.route("/gameover", methods = ["GET","POST"])
def game_over():
	if request.method == "POST":
		return render_template("/")
	return render_template("game_over.html")


if __name__ == '__main__':
	app.run(host=os.environ.get("IP"),
		port=int(os.environ.get("PORT")), 
		debug=True)
			
			