##generate flask structure
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['get'])
def api():
    return jsonify({'message': 'Hello World!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)