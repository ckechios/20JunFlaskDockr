from flask import Flask, request, jsonify

app = Flask(__name__)
DATA_FILE = 'data.txt'

@app.route('/')
def index():
    return {
        "message": "Welcome to the Phonebook API",
        "status": "ok"
    }, 200

@app.route('/add', methods=['GET'])
def addrec():
    # name = request.form.get('name')
    # number = request.form.get('number')
    name = request.args.get('name')
    number = request.args.get('number')
        
    with open(DATA_FILE, 'a') as f:
        f.write(f"{name},{number}\n")
    
    return jsonify({"status": "success", "message": "Record added"}), 201

@app.route('/list', methods=['GET'])
def list_all():
    try:
        with open(DATA_FILE, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return jsonify({"records": [], "status": "ok"})
    
    records = []
    for line in lines:
        parts = line.strip().split(',', 1)
        name, number = parts
        records.append({"name": name, "number": number})
    
    return jsonify({"records": records, "status": "ok"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
