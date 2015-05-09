from flask import *
from flask_wtf import Form
from forms import VoteForm
import sqlite3

#config
DATABASE = 'voting.db'
SECRET_KEY = 'U\xdc\x06\xce\xd0\xd6\xa0\xd8P]\xe9\x1cD\xc8+bS\xc7Y\xca\xae\xfb\xd1rW'


app = Flask(__name__)
 
app.config.from_object(__name__)

#connect to database
def connect_db():
  return sqlite3.connect(app.config['DATABASE'])

@app.route("/")
def home():
	return render_template("home.html")

#accepting of the vote from the user
@app.route('/vote', methods=['GET', 'POST'])
def vote():
  form = VoteForm()
 
  if request.method == 'POST':
      g.db = connect_db()
      k= request.form.get('opt1')
      w= request.form.get('opt2')
      s= request.form.get('opt3')
      b= request.form.get('opt4')
      
      for i in range (0,1):
        if k== 'opt1':
          g.db.execute("INSERT INTO vote VALUES('opt1')")
        if w=='opt2':
          g.db.execute("INSERT INTO vote VALUES('opt2')")
        if s=='opt3':
            g.db.execute("INSERT INTO vote VALUES('opt3')")
        if b=='opt4':
            g.db.execute("INSERT INTO vote VALUES('opt4')")
        
     
      g.db.commit()
      g.db.close()

  elif request.method == 'GET':
    return render_template('vote.html', form=form)

  return redirect("result")

#result page and updating
@app.route("/result")
def result():
  g.db= connect_db()
  cur=g.db.execute('select * from vote')
  j = [dict(casts=row[0]) for row in cur.fetchall()]
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
