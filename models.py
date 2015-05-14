from app import db

class VotePost(db.Model):

	__tablename__="vote"

	id= db.Column(db.Integer, primary_key=True)
	casts= db.Column(db.String, nullable=True)

	def __init__(self,casts):
		self.casts=casts

