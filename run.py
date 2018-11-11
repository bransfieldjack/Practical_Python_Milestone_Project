import os 
import time
import calendar
import json
import copy
import re
from flask import Flask, session, request, redirect, render_template
from collections import Counter


app = Flask(__name__)
app.secret_key = "secret"


# Start reuseable functions


# Reusable function for opening a file and writing to it
def write_file(filename, message):
	with open (filename, 'a') as file:
		file.writelines(message + "\n")


#Get all incorrect answers
def get_all_incorrect_answers():
	answers = []
	with open("data/incorrect_answers.txt", "r") as incorrect_answers:
			answers = [row for row in incorrect_answers]
			return answers[-8:]


#Get all online users
def get_all_online_users():
	users = []
	with open("data/users.txt", "r") as online_users:
			users = [row for row in online_users]
			return users[-8:]
			


#Get high scores
def scores():
	find = []
	with open("data/scores.txt", "r") as file:
		find = [row for row in file]
		return find

#End reusable functions		


@app.route("/", methods = ["GET", "POST"])
def index():
	
	#Welcome page, add username. 
	if request.method == "POST":
		username = request.form["username"]
		session["user"] = username
		return redirect(request.form["username"])
	return render_template("index.html")


@app.route("/<username>", methods = ["GET","POST"]) #Username passed from index function, value obtained from form post. 
def riddle(username):
	
	ts = calendar.timegm(time.gmtime())
	readable = time.ctime(ts)
		
	#Load the json file containing the riddles
	riddles = []
	with open("data/riddles.json", "r") as riddle_data:
		riddles = json.load(riddle_data)	
		#Set the index to 0 to display the first riddle in the list first
		index = 0
		score = 0
	
		if request.method == "POST":
			index = int(request.form["index"])	#Specify index to be an integer not a string or else will return a type error
			user_answer = request.form["answer"].lower()
			if riddles[index]["answer"] == user_answer:
				score += 1
				index += 1
			else:
				write_file("data/incorrect_answers.txt", "Username: {0},\n" "Answer: {1}\n" "Date: {2}\n" .format(username, user_answer, readable))
			
		if request.method == "POST":
			if index >= 8:
				write_file("data/scores.txt", "Username: {0},\n" "Games Won: {1}\n" "Date: {2}\n" .format(username, score, readable))
				return redirect("game_over")
	
	incorrect_answers = get_all_incorrect_answers()
	online_users = get_all_online_users()
	
	return render_template("riddles.html", riddle_question = riddles, index = index, online_users = online_users, incorrect_answers = incorrect_answers, username = username, score = score)
	
	
@app.route("/scoreboard", methods = ["GET","POST"])
def scoreboard():
	high_scores = scores()
	incorrect_answers = get_all_incorrect_answers()
	return render_template("scoreboard.html", high_scores = high_scores, incorrect_answers = incorrect_answers)
	
	
#Renders the game over page with scoreboard functionality called by the score function. 
@app.route("/game_over", methods = ["GET","POST"])
def game_over():
	
	high_scores = scores()
			
	return render_template("game_over.html", high_scores = high_scores)


if __name__ == '__main__':
	app.run(host=os.environ.get("IP"),
		port=int(os.environ.get("PORT")), 
		debug=True)