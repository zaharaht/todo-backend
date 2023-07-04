from flask import request,Blueprint,jsonify
from backend.db import db
from backend.Todos.todos import Todo
from datetime import datetime


#importing blueprints

todos=Blueprint('todos',__name__,url_prefix='/todos')

#getting all todos

@todos.route("/")
def get_all_todos():
    Todo.query.all()
    return jsonify({
        "sucess":True,
        "data":todos,
        "total":len("todos")

    }),200

#creating atodo
@todos.route("/create",methods=["GET","POST"])
def create_todo():
    data=request.get_json()
    if request.json=='POST':
        text=data['text']
        completed=data['completed']

#validations
    if not text:
        return jsonify({'please enter your todo text'}),400
    
    if not completed:
        return jsonify({'please complete your todo'})
    
    new_todo=Todo(text=text,completed=completed)

#inserting values
    db.session.add(new_todo)
    db.commit()
    return jsonify({"New todo created sucessfully"}),200
