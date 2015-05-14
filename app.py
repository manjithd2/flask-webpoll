from flask import *
from flask_wtf import Form
from flask.ext.sqlalchemy import SQLAlchemy
from forms import VoteForm
import sqlite3

#config
app = Flask(__name__)
app.secret_key=  'U\xdc\x06\xce\xd0\xd6\xa0\xd8P]\xe9\x1cD\xc8+bS\xc7Y\xca\xae\xfb\xd1rW'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting.db'


db=SQLAlchemy(app)

from models import *

#connect to database
def connect_db():
  return sqlite3.connect('voting.db')

@app.route("/")
def home():
	return render_template("home.html")

#accepting of the vote from the user
@app.route('/vote', methods=['GET', 'POST'])
def vote():
  form = VoteForm()
 
  if request.method == 'POST':
      k= request.form.get('opt1')
      w= request.form.get('opt2')
      s= request.form.get('opt3')
      b= request.form.get('opt4')
      
      if k== 'opt1':
        k=VotePost('opt1')
        db.session.add(k)
      if w=='opt2':
        w=VotePost('opt2')
        db.session.add(w)
      if s=='opt3':
        s=VotePost('opt3')
        db.session.add(s)
      if b=='opt4':
        b=VotePost('opt4')
        db.session.add(b)
     
      db.session.commit()

  elif request.method == 'GET':
    return render_template('vote.html', form=form)

  return redirect("result")

#result page and updating
@app.route("/result")
def result():
  g.db= connect_db()
  cur=g.db.execute('select * from vote')
  j = [dict(casts=row[1]) for row in cur.fetchall()]
  g.db.close()
  op1=0
  op2=0
  op3=0
  op4=0

  for d in j:
    for key in d:
      if d[key]=='opt1':
        op1=op1+1
      if d[key]=='opt2':
        op2=op2+1
      if d[key]=='opt3':
        op3=op3+1
      if d[key]=='opt4':
        op4=op4+1
  #incase something is above 100
  if op1>100 or op2>100 or op3>100 or op4>100:
    op1/100
    op2/100
    op3/100
    op4/100
  return render_template("result.html",opt1=op1,opt2=op2,opt3=op3,opt4=op4)

#random
@app.route("/<username>")
def user(username):
	return username

if __name__ == "__main__":
	app.run(debug=True)
