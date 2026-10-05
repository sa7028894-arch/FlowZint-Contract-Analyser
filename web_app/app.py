import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    print(f"DEBUG: Received User: {username}, Password: {password}")
    
    if username == "sa7028894@gmail.com" and password == "bawal111":
        return jsonify({"status": "success"})
    return jsonify({"status": "failed"})

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        analysis_results = {
            "vulnerabilities": ["Reentrancy Attack", "Integer Overflow", "Unchecked Call"],
            "severity": "High"
        }
        
        return render_template('results.html', results=analysis_results)

if __name__ == '__main__':
    app.run(debug=True)
