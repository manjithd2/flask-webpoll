from app import db
from models import VotePost

db.create_all()

db.session.add(VotePost("opt1"))
db.session.add(VotePost("opt2"))
db.session.add(VotePost("opt3"))
db.session.add(VotePost("opt4"))
db.session.add(VotePost("opt1"))
db.session.add(VotePost("opt2"))

db.session.commit()