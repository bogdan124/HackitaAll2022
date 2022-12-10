##generate flask structure
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['get'])
def api():
    object = {
        "subject":"",
        "locatie":"",
        "data":"",
        "prenume":"",
        "nume":"",
        "cnp":"",
        "email":"",
        "telefon":"",
        "comment":"",
    }
    return jsonify(object)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)