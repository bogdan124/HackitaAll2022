from typing import List, Dict
from flask import Flask, request, jsonify
import mysql.connector
import json



app = Flask(__name__)


def test_table(subject, locatie, data, prenume, nume, cnp, email, telefon, comment ) -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'devopsroles'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    data=cursor.execute("INSERT INTO appointment(subject, locatie, data, prenume, nume, cnp, email, telefon, comment ) VALUES('"+subject+"', '"+locatie+"','"+data+"', '"+prenume+"','"+nume+"', '"+cnp+"','"+email+"', '"+telefon+"','"+comment+"');")
    ##commit
    connection.commit()
    cursor.close()
    connection.close()
    return data


def data_testt():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'devopsroles'
    }
    connection = mysql.connector.connect(**config)
    ##select from appointments
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM appointment""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


@app.route('/',methods=["GET"])
def index() -> str:
    return json.dumps({'data': data_testt()})

##create an api route that takes the object variable writen up and is a post reuqest
@app.route('/api/add', methods=['get'])
def api_post():
    ##check for errors
    if request.method == 'GET':
        object = request.args
        if 'prenume' not in object or 'nume' not in object or 'cnp' not in object :
            return json.dumps({'error': 'Please fill in all the fields.'})
        if 'email' not in object or 'telefon' not in object or 'comment' not in object:
            return json.dumps({'error': 'Please fill in all the fields.'})
        if 'subject' not in object or 'locatie' not in object or 'data' not in object :
            return json.dumps({'error': 'Please fill in all the fields.'})
        else:
            subject = object['subject']
            locatie = object['locatie']
            data = object['data']
            prenume = object['prenume']
            nume = object['nume']
            cnp = object['cnp']
            email = object['email']
            telefon = object['telefon']
            comment = object['comment']
            test_table(subject, locatie, data, prenume, nume, cnp,
            email, telefon, comment)
            
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
@app.route('/api/colors/', methods=['get'])
def api_post_color():
    ##get data from get url parameters
    object = request.args  
    ##if you get no parameters return null
 
    if not object:
        return jsonify({
            "color": "null"
        })
    # generate 36 distinct pastel colours
    colors = distinctipy.get_colors(int(object['color_number']), 
                                    pastel_factor=float(object['pastel_factor']),
                                    n_attempts=int(object['attempts']))
    ##get all rgb and add them to a list of rgb colors
    rgb_list = []
    for i in range(0,len(colors)):
        rgb_list.append(distinctipy.get_rgb256(colors[i]))
    ##return rgb color list
    return jsonify({
        "rgbs": rgb_list
    })

  

if __name__ == '__main__':
    app.run(host='0.0.0.0')