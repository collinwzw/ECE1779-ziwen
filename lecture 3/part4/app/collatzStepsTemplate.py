"""
    4th Tutorial Session

"""

from flask import render_template, request
from app import webapp


@webapp.route('/collatz_template')
def collatz_template():
    """
    Create a web page with the number of steps it takes to reach 1, by applying 
    the two steps of the Collatz conjecture beginning from n.

    """

    if request.args.get('n').isdigit() == False:
        return "Error! All inputs most be of type int"

    n = original = int(request.args.get('n'))
    
    steps = []
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        steps.append(n)





@webapp.route('/collatz_form_template',methods=['GET'])
def collatz_form_template():

    return render_template("collatz_form.html")
