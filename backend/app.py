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
    ##add data to database
    return jsonify(object)  

##create an api route that takes the object variable writen up and is a post reuqest
@app.route('/api', methods=['get'])
def api_post():
    object = request.json
    subject = object['subject']
    locatie = object['locatie']
    data = object['data']
    prenume = object['prenume']
    nume = object['nume']
    cnp = object['cnp']
    email = object['email']
    telefon = object['telefon']
    comment = object['comment']
    
    return jsonify({
        "subject": subject,
        "locatie": locatie,
        "data": data,
        "prenume": prenume,
        "nume": nume,
        "cnp": cnp,
        "email": email,
        "telefon": telefon,
        "comment": comment
    })

##endpoint that is getting a post request with a tag color and is created a color pallet
@app.route('/api/<tag>', methods=['get'])
def api_post_color(tag):
    object = request.json
    color = object['color']


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)