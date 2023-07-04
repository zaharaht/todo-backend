
from backend import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    public_id=db.Column(db.String(50),unique=True)
    name=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(100))
    admin=db.Column(db.Boolean)

    def __init__(self,name,password,public_id,admin):
      self.name=name  
      self.public_id=public_id
      self.password=password
      self.admin=admin



def __repr__(self):
         return f"<user{self.name} >"