"""
    2nd Tutorial Session
    
    How to run this app:
    
    Option 1:

    1. Starting your web application -> From the menu on the top click 'Window' and then click 'New Terminal'
    2. Go the directory where the collatzSteps.py file is
    3. Type: python collatzSteps.py
    
    Option 2: Click the green run button.
    
    
    Instructions:

    1. Use the request object to get the number passed in via the url. Make sure to validate that the input is an integer or throw an error.
    2. Using the input integer compute and return the Collatz steps.
    3. Create a simple html snippet and it back to the user that shows the collantz steps for a given integer(See part2.jpg for what your output should look like, if you provided a value of 5)
    4. Find the public ip of your instance by using the following command: dig +short myip.opendns.com @resolver1.opendns.com
    5. You can see your webpage at the following example url (replace this ip with the one you got from step 3) http://3.231.155.231:5000/collatz?n=5


    
"""

import datetime
from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/collatz')
def collatz():
    """
    Create a web page with the number of steps it takes to reach 1, by applying 
    the two steps of the Collatz conjecture beginning from n.

    """


app.run(host='0.0.0.0')
    

