# Riddle Me This. Practical Python - Milestone Project.


## About: 
This is a 'Riddle Guessing Game' web app. 
The app displays a text based riddle to the user along with a form for the user to submit their answer.
If the user guesses the correct answer, they will progress to the next riddle. 
If the user guesses incorrectly, the form input will be cleared and the user will have an oppertunity to guess again.
More than one user can play at the same time, and they are identified by a unique username of their choosing upon arriving at the sites landing page/index.html. 
Upon completion of the game, (when all riddles have been aswered correctly) users will be able to view their results on a scoreboard, and there will be a corresponding "shameboard" where users can view all the icorrect answers as well.


Jack Bransfield - Code Institute, Full Stack Web Development. 
The project can be accessed from the following link: [riddle-project](https://riddle-project.herokuapp.com/)


## Site Navigation Description:
The user will arrive at the apps welcome page.
The welcome page contains a form for username submission. 
The user cannot progress throughout the site without selecting a username first. 
Once the user has input a name via the form submission, they will be redirected to the riddle game page. 
There is only one immediately visible clickable button on this page.
In the top left hand corner of the page, there is a clickable link to the sites scoreboard.
This link will redirect the user to a page containing a scoreboard on the left, and a shameboard on the right. 
The users username, games won/lost and a timestamp will be displayed on this page. 
The user can navigate back to the previous page using the browser, and there is also a button present with which the user can exit the game.
Exiting the game will redirect the user back to the login screen by default. 

The lower section of the riddle page of this game, displays a list of current online users on the left, and incorrect answers listed for each user.
This can be used as a guide throughout the game guessing process, to prevent a user using the same guess more than once. 
The riddle question is displayed on the centre of this page. 
Upon each successful riddle being guessed correctly, flask will display a new question on the page. 
This is done via a flask for loop, which incrementally iterates through a list of riddles stored in a json file. 
When the user has successfully answered all riddle questions correctly, they will be directed to the game_over page. 
Here the user will be given the oppertunity to play the game again, or view the scoreboard. 


## Technologies used and functionality:
Technologies used in this project include:
    
* Bootstrap: Bootstrap was used for a basic HTML template.
* HTML5/CSS: Used for the layout and styling of the application. 
* Python 3.0: The back end functionality of the application was written entirely in python 3.0.
* Flask Microframework: Flask was used to extend pythons functionality to the frond end. 
* Python unit testing was used to conduct unit tests of backend functionality. 
* Balsamiq Cloud: Used for wireframes.


## Other Sources
Images used for this project were taken from the pexels stock library:

[Pexels](https://www.pexels.com/)


## Automated testing
This project was created using a TDD approach.
Unit testing was conducted as much and as frequently as possible. 
For test cases where the unittest  framework could not be applied to the work, a seperate test_run.py file was used to test standalone python functions. 
The purpose of unit testing with python is to recognise bugs/issues with the code early on in the development process. 

### Unit testing in python

```
#Test No.1, to compare two values and return the result. 
    def test_equal(self):
        expected = "test"
        actual = "test"
        self.assertEqual(expected, actual)
```
```
#Test No.2, open a text file and write a value to it. 
    def test_write_to_file(self):
        file = "/test_file.txt"
        value = "test"
        with open (file, "w") as f:
            f.writelines(value + "\n")
        v = [row for row in f]
        self.assertEqual(v, f)
        print("test_ran")
```
```
#Test No.3 (Part-One), to compare that the value retrieved from a text file is as expected. 
    def test_file(self):
        file = "/test_file.txt"
        value = "test"
        with open (file) as f:
            v = [row for row in f]
            self.assertEqual(v, value)
```

[I/O operation on a closed file.](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/input_output_operation_on_closed_file.PNG)

[Read/Write permissions granted.](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/read_write_permissions_granted_text_file.PNG)

[Value not expected.](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/value_not_expected.PNG)


### Custom Python Test Functions
 
 
## Manual Testing


Linking/pages:

Checked all outgoing (page to page) and internal links (form submission button).
Confirmed that no orphan pages exist as part of this project. (Un-used pages left over from the development process)

Form Testing:

Tested form submission link.

Cookies Testing:

Disabled cookies and confirmed that the site behaves as per normal.
No observable effect on application security after disabling cookies during or outside of a session.

HTML Validation:

Validated all HTML code using: https://validator.w3.org/ (Fixed minor errors/warnings)

Database Testing:

Not applicable.

Ease of Learning:

The app is quite minimal. Everything the user needs in terms of information is clearly displayed. Clickable links are made obvious when appropriate.

Navigation:

The site is relatively easy to navigate. 
The user cannot progress throughout the game without entering a username. 
The sites scoreboard can be accessed via the link provided. 

Compatability:

Cross browser compatability testing has been conducted using Chrome, Firefox, Edge and Opera.
Mobile compatability testing has been undertaken to ensure that the site works well on mobile devices. 


## Wireframe/Design:
Wireframing for this app was done using Balsamiq Mockups (Web based).
Files were transferred to Cloud 9 from my local machine.


## Deploying the project:


## Examples of Code Refactoring:

Changed condition on when the riddles are no longer displayed by removing:
    
    ~~~~
    if request.method == "POST":
			if user_answer == "palmtree" and index >= 7:
				return redirect("game_over")
    ~~~~
    
Replacing with:
   
    ~~~~
    if request.method == "POST":
			if index >= 8:
				return redirect("game_over")
	~~~~
	