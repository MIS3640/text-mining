## Instructions - how to run this code/web app
## If you do not want to run the code on your machine, I've included a youtube link to a video demo of the web-app in action
## 

1. Add Venmo information to sensitive.txt, if you don't have Venmo or you're not comfortable doing this I'm happy to schedule a 
virtual demo where I can demonstrate the web app using my Venmo credentials
File contents should look like:
{"username": "YourUsername", "password": "YourPassword"}

2. Run venmo_functions.py

3. You should receive a text notification on your phone from Venmo with an activation code, 
type this activation code into the Visual Studio Code terminal where it prompts you for an input

4. Navigate to directory where this code is installed through command prompt
for me this is: C:\Users\mnorian1\Downloads\text-mining>

5. Activate virtual environment using venv\Scripts\activate
C:\Users\mnorian1\Downloads\text-mining> venv\Scripts\activate

6. Set the flask app by typing set FLASK_APP = app.py
(venv) C:\Users\mnorian1\Downloads\text-mining> set FLASK_APP = app.py

7. Run the flask server by typing flask run
(venv) C:\Users\mnorian1\Downloads\text-mining> flask run

8. In the browser, navigate to http://127.0.0.1:5000/

9. All of your Venmo notes statistics should be displayed on the screen!




