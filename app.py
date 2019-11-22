import datetime
import os

from flask import Flask, render_template, redirect, url_for
from forms import ItemForm
from models import Items
from database import db_session
#This module is responsible for adding functionality to the root and the success page

app = Flask(__name__)
app.secret_key = os.environ['APP_SECRET_KEY']


#This adds functionality to the rootpage 
#The root page has the function add item which calls an itemform 
#If the submission is successful the form will: 
    #add the Items into the variable "item"
    #The item is then added to the database
    #page is redirected to the success page
@app.route("/", methods=('GET', 'POST'))
def add_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(name=form.name.data, quantity=form.quantity.data, description=form.description.data, date_added=datetime.datetime.now())
        db_session.add(item)
        db_session.commit()
        return redirect(url_for('success'))
    return render_template('index.html', form=form)
#Initially the code did not read the actual database
@app.route("/success")
def success():
    results = []
 
    qry = db_session.query(Items)
    allitems=qry.all()
#Modified code:added for loop to read out all entries in the database on the success page 
    for i in range(len(qry.all())):
         entry=allitems[i].id, allitems[i].name, allitems[i].quantity, allitems[i].description, allitems[i].date_added
         results.append(str(entry))
    return str(results)
   
  
#This runs the code in python. Added debug=True to allow for debugging of code and port='5001' to be able to communicate with nginx
if __name__ == '__main__':
    app.run(host='0.0.0.0', port ='5001', debug=True)
