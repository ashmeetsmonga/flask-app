from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

PORT = 5000

@app.route('/')
def hello_world():
    todo = Todo(title='First Todo', desc='This is first todo')
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')

@app.route('/show')
def todos():
    allTodos = Todo.query.all()
    print(allTodos)
    return 'Products Page'

if __name__ == '__main__':
    app.run(debug=True, port=PORT)