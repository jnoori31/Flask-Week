from flask import Flask
import math

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/square/<int:number>')
def square(number):
    answer = math.pow(number,2)
    result = int(answer)
    return str(result)
       

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)