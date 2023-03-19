from flask import Flask, render_template
app = Flask(__name__)

PORT = 5000

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/products')
def products():
    return 'Products Page'

if __name__ == '__main__':
    app.run(debug=True, port=PORT)