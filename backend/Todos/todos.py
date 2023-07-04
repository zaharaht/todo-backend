
from backend import db

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(20))
    completed=db.Column(db.Boolean)

    def __init__(self,text,completed):
      self.text=text  
      self.completed=completed
      



def __repr__(self):
         return f"<Todo{self.text} >"