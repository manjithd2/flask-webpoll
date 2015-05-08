from flask.ext.wtf import Form
from wtforms.fields import *

class VoteForm(Form):
  opt1 = BooleanField("Option 1")
  opt2 = BooleanField("Option 2")
  opt3 = BooleanField("Option 3")
  opt4 = BooleanField("Option 4")
  submit = SubmitField("submit")