from flask import render_template, request
from app import webapp


@webapp.route('/add_template',methods=['GET','POST'])
def add_template():
    if request.args.get('n1').isdigit() == False or \
       request.args.get('n2').isdigit() == False:
        return "Error! All inputs most be of type int"
    
    n1 = int(request.args.get('n1'))
    n2 = int(request.args.get('n2'))

    return render_template("add.html",n1=n1,n2=n2,result=n1+n2)

@webapp.route('/add_form_template',methods=['GET'])
def add_form_template():
    return render_template("add_form.html")



