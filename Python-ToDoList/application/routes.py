from application import app, db
from application.models import Todos
from flask import render_template

@app.route('/', methods=['Get'])
@app.route('/index', methods=['GET'])
def index():
   # all_todos= Todos.query.all()
    incomplete = Todos.query.filter_by(state=False).all()
    complete = Todos.query.filter_by(state=True).all()
    number_of_todos = Todos.query.count()
    return render_template('index.html')


@app.route('/get/<id>/', methods=['GET'])
def post_details(id):
    task = Todos.query.get(id)
    return


@app.route('/add', methods=['POST'])
def add_task():
    todo = Todos(title, body)
    db.session.add(todo)
    db.session.commit()


@app.route('/update/<id>/', methods=['PUT'])
def update_article(id):
    todo = Todos.query.get(id)
    todo.title = title
    todo.body = body
    db.session.commit()


@app.route('/delete/<id>/', methods=['DELETE'])
def article_delete(id):
    todo = Todos.query.get(id)
    db.session.delete(todo)
    db.session.commit()


@app.route('/complete/<id>')
def complete(id):
    todo = Todos.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    return "You have completed this task"


@app.route('/incomplete/<id>')
def incomplete(id):
    todo = Todos.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    return "You have not completed this task"
