"""
    First Tutorial Session 1

    How to run this app:
    
    Option 1:

    1. Starting your web application -> From the menu on the top click 'Window' and then click 'New Terminal'
    2. Go the directory where the current_time.py file is
    3. Type: python current_time.py
    
    Option 2: Click the green run button.
    
    
    Instructions:
    
    1. Define a new function and get the current time from the datetime object
    2. Create a simple html page that shows the current time with a refresh link(See part1.jpg for what your output should look like)
    3. Find the public ip of your instance by using the following command: dig +short myip.opendns.com @resolver1.opendns.com
    4. You can see your webpage at the following example url (replace this ip with the one you got from step 3) http://3.231.155.231:5000/time


"""


import datetime  #package includes functions that provide day and time info

from flask import Flask
app = Flask(__name__)

@app.route('/time')




app.run(host='0.0.0.0')