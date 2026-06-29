from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock Database
users_db = {"admin": "password123"} 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if users_db.get(data['username']) == data['password']:
        return jsonify({"status": "success"})
    return jsonify({"status": "fail"}), 401

if __name__ == '__main__':
    app.run(debug=True)