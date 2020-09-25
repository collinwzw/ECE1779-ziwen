"""
    2n Tutorial Session
"""

from flask import render_template, request
from app import webapp



@webapp.route('/collatz')
def collatz():
    """
    Create a web page with the number of steps it takes to reach 1, by applying 
    the two steps of the Collatz conjecture beginning from n.

    """

# student code starts here

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

    series = str(original)

    for i in steps:
        series = series + "->" + str(i)

    html = """
        <!DOCTYPE html >
            <body>
                <p>Collantz series for {0} </p>
                <p>{1}</p>
                <p>Number of steps = {2}</p>
            </body>
        </html>
    """

    return html.format(original,series,len(steps))

#end of student code


