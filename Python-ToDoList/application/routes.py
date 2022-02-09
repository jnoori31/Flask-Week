from application import app, db
from application.models import Todos
# render_templates, request


@app.route('/index', methods=['GET'])
def index():
   # all_todos= Todos.query.all()
 incomplete = Todos.query.filter_by(state=False).all()
 complete = Todos.query.filter_by(state=True).all()
 return render_templates('index.html')


@app.route('/get/<id>/', methods=['GET'])
def post_details(id):
    task = Todos.query.get(id)
    return article_schema.jsonify(article)


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


app.route('/complete/<id>')
def complete(id):
    todo = Todos.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
