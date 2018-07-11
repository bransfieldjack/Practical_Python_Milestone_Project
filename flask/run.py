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
Add new users to the users file
"""
def new_user(username):
	write_file("files/users.txt", username)
	

@app.route("/", methods = ["GET", "POST"])
def index():
	"""
	Welcome page, add username. 
	"""
	if request.method == "POST":
		new_user(request.form["username"])
		return redirect(request.form["username"])
	return render_template("index.html")


@app.route("/<username>", methods = ["GET","POST"]) #Username passed from index function, value optaine from form post. 
def riddle(username):
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
				write_file("files/correct_answers.txt", user_answer + username)
			else:
				write_file("files/incorrect_answers.json", user_answer + username)
			
			
		if request.method == "POST":
			if user_answer == "palmtree" and index >= 7:
				return render_template("game_over.html")
			
			
	with open("files/users.txt", "r") as users:
		online_users = users.read(100000) 
			
	
	with open("files/correct_answers.txt", "r") as answers:
		correct_answers = answers.read(100000)
			
			
	with open("files/incorrect_answers.txt", "r") as incorrect:
		incorrect_answers = incorrect.read(100000)
			
			
	return render_template("riddles.html", riddle_question = riddles, index = index, online_users = online_users, correct_answers = correct_answers, incorrect_answers = incorrect_answers, username = username)
	
	
@app.route("/gameover", methods = ["GET","POST"])
def game_over():
	if request.method == "POST":
		return render_template("/")
	return render_template("game_over.html")


if __name__ == '__main__':
	app.run(host=os.environ.get("IP"),
		port=int(os.environ.get("PORT")), 
		debug=True)