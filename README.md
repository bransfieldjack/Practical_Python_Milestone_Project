# Riddle Me This. Practical Python - Milestone Project.


## Jack Bransfield - Code Institute, Full Stack Web Development. 
The project can be accessed from the following link: [riddle-project](https://riddle-project.herokuapp.com/)


### What the project does:
This is a 'Riddle Guessing Game' web app. 
The app displays a text based riddle to the user along with a form for the user to submit their answer.
If the user guesses the correct answer, they will progress to the next riddle. 
If the user guesses incorrectly, the form will be cleared and the user will have an oppertunity to guess again.
More than one user can play at the same time, and they are identified by a unique username of their choosing. 
Upon completion of the game, (when all riddles have been aswered correctly) users will be able to view their results on a scoreboard. 


### Technologies used and functionality:
Technologies used in this project include:
    
* Bootstrap: Bootstrap was used for a basic HTML template.
* HTML5/CSS: Used for the layout and styling of the application. 
* Python 3.0: The back end functionality of the application was written entirely in python 3.0.
* Flask Microframework: Flask was used to extend pythons functionality to the frond end. 
* Balsamiq Cloud: Used for wireframes.


### Testing:


### Wireframe/Design:
Wireframing for this app was done using Balsamiq Mockups (Web based).
Files were transferred to Cloud 9 from my local machine.


### Deploying the project:


### Code Refactoring:

Changed condition on when the riddles are no longer displayed by removing:
    
    ```
    if request.method == "POST":
			if user_answer == "palmtree" and index >= 7:
				return redirect("game_over")
    ```
    
Replacing with:
    
    ```
    if request.method == "POST":
			if index >= 8:
				return redirect("game_over")
	```