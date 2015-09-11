from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/test')
def Testing():
    return "Test complete"
    
@app.route('/user/login', methods=["GET", "POST"])
def login():
    return
    
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)