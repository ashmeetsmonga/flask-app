from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

PORT = 5000

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/products')
def products():
    return 'Products Page'

if __name__ == '__main__':
    app.run(debug=True, port=PORT)