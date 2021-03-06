# Riddle Me This. Practical Python - Milestone Project.


## About: 
This is a 'Riddle Guessing Game' web app. 
The app displays a text-based riddle to the user along with a form for the user to submit their answer.
If the user guesses the correct answer, they will progress to the next riddle. 
If the user guesses incorrectly, the form input will be cleared, and the user will have an opportunity to guess again.
More than one user can play at the same time, and they are identified by a unique username of their choosing upon arriving at the sites landing page/index.html. 
Upon completion of the game, (when all riddles have been answered correctly) users will be able to view their results on a scoreboard, and there will be a corresponding "shame board" where users can view all the incorrect answers as well.


The project can be accessed from the following link: [riddle-project](https://riddle-project.herokuapp.com/)


## Site Navigation Description:
The user will arrive at the apps welcome page.
The welcome page contains a form for username submission. 
The user cannot progress throughout the site without selecting a username first. 
Once the user has input a name via the form submission, they will be redirected to the riddle game page. 
There is only one immediately visible clickable button on this page.
In the top left-hand corner of the page, there is a clickable link to the site’s scoreboard.
This link will redirect the user to a page containing a scoreboard on the left, and a shame board on the right. 
The user's username, games won/lost, and a timestamp will be displayed on this page. 
The user can navigate back to the previous page using the browser, and there is also a button present with which the user can exit the game.
Exiting the game will redirect the user back to the login screen by default. 

The lower section of the riddle page of this game displays a list of current online users on the left, and incorrect answers listed for each user.
This can be used as a guide throughout the game guessing process, to prevent a user using the same guess more than once. 
The riddle question is displayed in the centre of this page. 
Upon each successful riddle being guessed correctly, flask will display a new question on the page. 
This is done via a flask for loop, which incrementally iterates through a list of riddles stored in a JSON file. 
When the user has successfully answered all riddle questions correctly, they will be directed to the game over page. 
Here the user will be given the opportunity to play the game again or view the scoreboard. 


## Technologies used and functionality:
Technologies used in this project include:
    
* Bootstrap: Bootstrap was used for a basic HTML template.
* HTML5/CSS: Used for the layout and styling of the application. 
* Python 3.0: The back-end functionality of the application was written entirely in python 3.0.
* Flask Microframework: Flask was used to extend pythons functionality to the front end. 
* Python unit testing was used to conduct unit tests of backend functionality. 
* Balsamiq Cloud: Used for wireframes.


## Other Sources
Images used for this project were taken from the pexels stock library:

[Pexels](https://www.pexels.com/)

*All of the code written in this project is my own.

## Automated testing
This project was created using a TDD approach.
Unit testing was conducted as much and as frequently as possible. 
For test cases where the unit test framework could not be applied to the work, a separate test_run.py file was used to test standalone python functions. 
The purpose of unit testing with python is to recognise bugs/issues with the code early in the development process. 


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

!["I/O operation on a closed file."](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/input_output_operation_on_closed_file.PNG)


!["Read/Write permissions granted."](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/read_write_permissions_granted_text_file.PNG)


!["Value not expected."](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/value_not_expected.PNG)


### Custom Python Test Functions
 
 
```
#Non-python-unit testing functions:
    
#Compare that the value retrieved from a text file is as expected. 
def test_file_2(file, value):
    with open(file) as f:
        f.writelines(value + "\n")
    if value == f:
        print("Test has completed with success. ")
```
```
def test_riddle_file(file, value):
    riddles = []
    with open(file, "r") as riddle_data:
        riddles = json.load(riddle_data)    
                
    if riddles == value:
        print("Test is completing with success. ")
```
```
test_file_2(file="test_file.txt", value="test")
test_riddle_file(file="test_riddles.json", value="test")
```
 
 
## Manual Testing


### Linking/pages:

Checked all outgoing (page to page) and internal links (form submission button).
Confirmed that no orphan pages exist as part of this project. (Un-used pages left over from the development process)

### Form Testing:

Tested form submission link.

### Cookies Testing:

Disabled cookies and confirmed that the site behaves as per normal.
No observable effect on application security after disabling cookies during or outside of a session.

### HTML Validation:

Validated all HTML code using: https://validator.w3.org/ (Fixed minor errors/warnings)

### Database Testing:

Not applicable.

### Ease of Learning:

The app is quite minimal. Everything the user needs in terms of information is clearly displayed. Clickable links are made obvious when appropriate.

### Navigation:

The site is relatively easy to navigate. 
The user cannot progress throughout the game without entering a username. 
The sites scoreboard can be accessed via the link provided. 

### Compatibility:

Cross browser compatibility testing has been conducted using Chrome, Firefox, Edge and Opera.
Mobile compatibility testing has been undertaken to ensure that the site works well on mobile devices. 


## Wireframe/Design:
Wireframing for this app was done using Balsamiq Mock-ups (Web-based).
Files were transferred to Cloud 9 from my local machine.


![](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/index_page.PNG)
![](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/riddle_page.PNG)
![](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/game_over_page.PNG)


## Deploying the project:
This app is currently being hosted on Heroku. 
Instructions for deploying the code are as follows:

### From the Heroku Dashboard:

* Login to your heroku account.
* From the dashboard, select: New > Create New App.
* Select an appropriate App Name as per the on-screen instructions, and the most relevant hosting region. 
* Select Create App.

### From the bash command line/local repo:

* Logon to your heroku account using the 'heroku login' command. 
* Initialise your repo, if you havent already done so.
* Connect the Heroku App repo using the 'heroku git:remote -a (app name)' command.
* In order for Heroku to build your app, you will need to specify the requirements using the following command: 'sudo pip3 freeze --local > requirements.txt'.
* You will also need to generate a "Procfile" before pushing your code. This acts as the entry point for your application. To generate this file, use the 'echo web: python app.py > Procfile' command from bash.
* Use git add. to save your work.
* Add your first commit (git commit -m "Initial Commit. "), then use 'git push heroku master' to push your code to Heroku. 
* To complete the process and ensure that your app will run, set the appropriate config variables from the heroku settings tab. 
* Create an 'IP' config var, with a corresponding value of: 0.0.0.0.
* Create a 'PORT' config var, with a corresponding value of: 5000.
* To access the application, click open on the heroku console (top right) and record the apps URL. 

## Examples of Code Refactoring:

### Changed condition on when the riddles are no longer displayed by removing:
    
    ```
    if request.method == "POST":
            if user_answer == "palmtree" and index >= 7:
                return redirect("game_over")
    ```
    
### Replacing with:
   
    ```
    if request.method == "POST":
            if index >= 8:
                return redirect("game_over")
    ```
