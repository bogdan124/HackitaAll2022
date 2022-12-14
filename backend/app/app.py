from typing import List, Dict
from flask import Flask, request, jsonify, url_for,render_template
import mysql.connector
import json
import os
 



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


##add location data.json from static
@app.route('/api/locations/', methods=['get'])
def api_post_locations():
    STOREA_DATA =[
	{
		"latitude": 44.1993965,
		"longitude": 27.3188548,
		"title": "BCR Calarasi",
		"description": "Strada Prelungirea Bucuresti, nr. 6, bl. N1, parter, Calarasi, Calarasi",
		"zoomLevel": 16
	},
	{
		"latitude": 46.0739387,
		"longitude": 23.5753362,
		"title": "BCR Alba",
		"description": "Str. Tudor Vladimirescu, nr.1, Alba-Iulia, judetul Alba, Alba Iulia, Alba",
		"zoomLevel": 16
	},
	{
		"latitude": 46.363040,
		"longitude": 23.050750,
		"title": "BCR Campeni",
		"description": "Piata Avram Iancu nr.8, Campeni, Alba",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.098000,
		"longitude": 27.182810,
		"title": "BCR Adjud",
		"description": "Strada Republicii nr. 28 bl. 85 parter., Adjud, Vrancea",
		"zoomLevel": 16
	},
	{
		"latitude": 45.2623659,
		"longitude": 27.9651153,
		"title": "BCR Braila",
		"description": "Calea Calarasilor, nr.53, Braila, Braila",
		"zoomLevel": 16 
	},
	{
		"latitude":44.9311218,
		"longitude": 25.4450356,
		"title": "BCR Nicu Circiumarescu",
		"description": "Bulevardul Mircea cel Batran nr.1, Targoviste, Dambovita",
		"zoomLevel": 16
	},
	{
		"latitude": 44.112110,
		"longitude": 24.347170,
		"title": "BCR Caracal",
		"description": "Strada N.Titulescu nr. 13, Caracal, Olt",
		"zoomLevel": 16
	},
	{
		"latitude": 44.6742125,
		"longitude": 25.4859898,
		"title": "BCR Corabia",
		"description": "Strada Tudor Vladimirescu Bl 1, Corabia, Olt",
		"zoomLevel": 16
	},
	{
		"latitude": 44.6742125,
		"longitude": 25.4859898,
		"title": "BCR Olt",
		"description": "Strada Basarabilor nr. 1, Slatina, Olt",
		"zoomLevel": 16
	},
	{
		"latitude": 47.1790258,
		"longitude": 23.0502718,
		"title": "BCR Salaj",
		"description": "Strada Simion-Oros (1885-1972), nr.4, Zalau, Salaj",
		"zoomLevel": 16
	},
	{
		"latitude": 47.2316996,
		"longitude": 22.7969109,
		"title": "BCR Simleul Silvaniei",
		"description": "Strada 1 Decembrie nr. 1918 Bl. D 1 parter, Simleu Silvaniei, Salaj",
		"zoomLevel": 16
	},
	{
		"latitude": 45.68259632088786, 
		"longitude":21.90196761101878,
		"title": "BCR Lugoj",
		"description": "Strada Cuza Voda nr. 4, Lugoj, Timis",
		"zoomLevel": 16
	},
	{
		"latitude": 44.4092832,
		"longitude": 26.0958648,
		"title": "BCR Serban Voda",
		"description": "Calea Serban Voda nr.209, Bucuresti, Sector 4",
		"zoomLevel": 16
	},
	{
		"latitude": 46.31247894004557, 
		"longitude": 23.71893690370384,
		"title": "BCR Aiud",
		"description": "Strada Transilvaniei Bl. A 13, Aiud, Alba",
		"zoomLevel": 16
	},
	{
		"latitude": 45.8446539119806,
		"longitude": 23.359267541418085,
		"title": "BCR Cugir",
		"description": "Strada Alexandru Sahia nr.23 Bl.S 6 bc, Cugir, Alba",
		"zoomLevel": 16 
	},
	{
		"latitude": 45.95767514066994, 
		"longitude": 23.569745082193485,
		"title": "BCR Sebes",
		"description": "Strada Mihai Viteazu nr.2, Sebes, Alba",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.6560083,
		"longitude": 24.6628694,
		"title": "BCR Borsa",
		"description": "Strada Decebal nr. 4 Bl. A1, Borsa, Maramures",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.6507194,
		"longitude": 23.0004454,
		"title": "BCR Iza",
		"description": "Bulevardul Republicii nr. 15, Baia Mare, Maramures",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.6551182,
		"longitude": 23.5674573,
		"title": "BCR Maramures",
		"description": "str. Culturii, nr.3, Baia Mare, judetul Maramures, Baia Mare, Maramures",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.6551254,
		"longitude": 23.5674573,
		"title": "BCR Sighetu Marmatiei",
		"description": "Piata 1 Decembrie 1918 nr.23, Sighetu Marmatiei, jud Maramures, Sighetu Marmatiei, Maramures",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.5497647,
		"longitude": 23.8876842,
		"title": "BCR Campia Turzii",
		"description": "Strada George Cosbuc nr.13, CampiaTurzii, Cluj",
		"zoomLevel": 16
	},
	{
		"latitude": 46.768062, 
		"longitude": 23.603054,
		"title": "BCR Cipariu",
		"description": "Strada Nicolae Titulescu nr.4 Bl. IIB Corp B3 parter, Cluj Napoca, Cluj",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.864544, 
		"longitude": 23.027017,
		"title": "BCR Huedin",
		"description": "Strada Republicii nr.8 bloc A S.C.2 parter, Huedin, Cluj",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.755100, 
		"longitude": 23.557904,
		"title": "BCR Manastur",
		"description": "Strada Bucegi nr.13-15, Cluj Napoca, Cluj",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.569089, 
		"longitude": 23.785905,
		"title": "BCR Turda",
		"description": "Piata 1 Decembrie 1918 nr.29, Turda, Cluj",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.5692062,
		"longitude": 23.7158495,
		"title": "BCR Cluj",
		"description": "Bulevardul 21 Decembrie 1989, nr.77 (The Office, cladirea A-B), Cluj Napoca, Cluj",
		"zoomLevel": 16
	},
	{
		"latitude": 47.142616, 
		"longitude": 23.873560,
		"title": "BCR Dej",
		"description": "Strada Bobalna nr.5, Dej, Cluj",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.176982826028, 
		"longitude": 24.17174626451053,
		"title": "BCR Beclean",
		"description": "Strada Mihail Kogalniceanu nr.46, Beclean, Bistrita-Nasaud",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.13688046529057, 
		"longitude": 24.498875487926842,
		"title": "BCR Bistrita Nasaud",
		"description": "Piata Petru Rares nr.17, Bistrita, Bistrita, Bistrita-Nasaud",
		"zoomLevel": 16
	},
	{
		"latitude": 45.12433997857637, 
		"longitude": 25.734205981680304,
		"title": "BCR Nasaud",
		"description": "Bulevardul Granicerilor nr.27, Nasaud, Bistrita-Nasaud",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.12682637387757, 
		"longitude": 24.48051563991147,
		"title": "BCR Viisoara",
		"description": "Strada Imparatul Traian nr.57 bloc E parter, Bistrita, Bistrita-Nasaud",
		"zoomLevel": 16 
	},
	{
		"latitude": 45.698765780740025, 
		"longitude": 27.190807679516094,
		"title": "BCR Vrancea", 
		"description": "Strada Fundatura Cuza Voda nr. 1, Focsani, Vrancea",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.564380414614966,
		"longitude":  26.91612798592077,
		"title": "BCR Bacau",
		"description": "Strada 9 Mai nr.11, Bacau, Bacau",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.5737532,
		"longitude": 26.9096448,
		"title": "BCR Bacovia",
		"description": "Strada Mioritei nr.1, Bacau, Bacau",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.421233223503634, 
		"longitude": 26.440187494245016,
		"title": "BCR Comanesti", 
		"description": "Strada Republicii nr.18, Comanesti, Bacau",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.524225,
		"longitude": 26.5618658,
		"title": "BCR Moinesti",
		"description": "Strada Zorilor nr.23, Moinesti, Bacau",
		"zoomLevel": 16
	},
	{
		"latitude": 46.244260180107915, 
		"longitude": 26.763391868712592,
		"title": "BCR Onesti",
		"description": "Strada Belvedere nr.1, Onesti, Bacau",
		"zoomLevel": 16
	},
	{
		"latitude": 47.1738659,
		"longitude": 27.5524084,
		"title": "BCR Pacurari",
		"description": "Soseaua Pacurari nr.137 Bl.600 parter, Iasi, Iasi",
		"zoomLevel": 16
	},
	{
		"latitude": 47.1738974,
		"longitude": 27.5370875,
		"title": "BCR Pascani",
		"description": "Strada St.cel Mare nr. 5, Pascani, Iasi",
		"zoomLevel": 16
	},
	{
		"latitude": 47.21130682800195,
		"longitude":  27.27246925232646,
		"title": "BCR Podu Iloaiei",
		"description": "Strada Nationala Bl.14 parter, Comuna Podu Iloaiei, Iasi",
		"zoomLevel": 16
	},
	{
		"latitude": 47.163014759501934, 
		"longitude":27.581830751501673,
		"title": "BCR A. I. Cuza",
		"description": "Bulevardul Stefan cel Mare si Sfant nr.8 Bl.A, Iasi, Iasi",
		"zoomLevel": 16
	},
	{
		"latitude": 47.1565146,
		"longitude": 27.5839427,
		"title": "BCR Iasi", 
		"description": "Strada Palat nr. 11, Iasi, Iasi",
		"zoomLevel": 16
	},
	{
		"latitude": 47.156529,
		"longitude": 27.5839427,
		"title": "BCR Botosani",
		"description": "Piata Revolutiei nr.9, Botosani, Botosani",
		"zoomLevel": 16
	},
	{ 
		"latitude": 47.1565435,
		"longitude": 27.5839427,
		"title": "BCR Dorohoi",
		"description": "Strada Grigore Ghica nr.30, Dorohoi, Botosani",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.7425646,
		"longitude": 26.6431489,
		"title": "BCR Primaverii",
		"description": "Strada Primaverii nr.16, Botosani, Botosani",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.7425823,
		"longitude": 26.6365828,
		"title": "BCR Campulung Moldovenesc",
		"description": "Calea Transilvaniei nr. 6, Campulung Moldovenesc, Suceava",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.7426105,
		"longitude": 26.6365828,
		"title": "BCR Falticeni",
		"description": "Strada Sucevei, Falticeni, Suceava",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.5536183,
		"longitude": 25.8862365,
		"title": "BCR Gura Humorului",
		"description": "Strada Republicii nr. 19 Bl. T 850 parter, Gura Humorului, Suceava",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.7057659,
		"longitude": 25.7001611,
		"title": "BCR Radauti",
		"description": "Strada Unirii nr. 65, Radauti, Suceava",
		"zoomLevel": 16 
	},
	{
		"latitude": 47.6417551,
		"longitude": 26.2537369,
		"title": "BCR Suceava" ,
		"description": "Strada Stefan cel Mare nr. 31, Suceava, Suceava",
		"zoomLevel": 16
	},
	{
		"latitude":  47.6417863,
		"longitude": 26.238416,
		"title": "BCR Vatra Dornei",
		"description": "Strada M.Eminescu nr. 35, Vatra Dornei, Suceava",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.91155782904196, 
		"longitude": 26.089061584082764,
		"title": "BCR Bicaz",
		"description": "Strada Barajului nr. 2A, Bicaz, Neamt",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.9242696,
		"longitude": 26.3741783,
		"title": "BCR Neamt",
		"description": "Bulevardul Traian nr. 19, Piatra Neamt, Neamt",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.9242769,
		"longitude": 26.3741783,
		"title": "BCR Roman",  
		"description": "Bulevardul Roman Musat nr.34, Roman, Neamt",
		"zoomLevel": 16 
	},
	{
		"latitude": 46.9242841,
		"longitude": 26.3741783,
		"title": "BCR Targu Neamt",
		"description": "Strada Mihail Kogalniceanu nr. 4, Targu Neamt, Neamt",
		"zoomLevel": 16
	},
	{
		"latitude": 44.89456111302473, 
		"longitude": 28.72530119303132,
		"title": "BCR Babadag",
		"description": "Strada Republicii nr.88 parter, Babadag, Tulcea",
		"zoomLevel": 16 
	},
	{
		"latitude": 45.2445198,
		"longitude": 28.129299,
		"title": "BCR Macin",
		"description": "Strada 1 Decembrie nr. 10 Bl. 17, Macin, Tulcea",
		"zoomLevel": 16
	},
    {
        "latitude": 45.1560122,
        "longitude": 29.6523163,
        "title": "BCR Sulina", 
        "description": "Strada a II a nr. 274, Sulina, Tulcea",
        "zoomLevel": 16
    },
    {
        "latitude": 45.172846495420146, 
        "longitude": 28.79786949750701,
        "title": "BCR Tulcea",
        "description": "Strada Toamnei nr. 2, Tulcea, Tulcea",
        "zoomLevel": 16
    },
    {
        "latitude": 44.4421388,
        "longitude": 26.848079,
        "title": "BCR Lehliu Gara",
        "description": "Strada Nicolae Titulescu nr.5D, Lehliu Gara, Calarasi",
        "zoomLevel": 16
    },
    {
        "latitude": 44.086096,
        "longitude": 26.6377478,
        "title": "BCR Oltenita",
        "description": "Bulevardul Republicii nr.56, Oltenita, Calarasi",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.4153341,
        "longitude": 27.8210049,
        "title": "BCR Fetesti",
        "description": "Strada Calarasi nr. 550, Fetesti, Ialomita",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.5623543,
        "longitude": 27.3665222,
        "title": "BCR Ialomita", 
        "description": "Strada Matei Basarab Bl. D6 scara B parter, Slobozia, Ialomita",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.640691,
        "longitude": 27.6545937,
        "title": "BCR Tandarei",
        "description": "Strada Bucuresti Bl. 57F parter, Tandarei, Ialomita",
        "zoomLevel": 16 
    },
    { 
        "latitude": 44.7152001,
        "longitude": 26.6419373,
        "title": "BCR Urziceni",
        "description": "Calea Bucuresti nr. 42, Urziceni, Ialomita",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.514152,
        "longitude": 26.78594,
        "title": "BCR Cernavoda",
        "description": "Strada Unirii Bl. P3B parter, Cernavoda, Constanta",
        "zoomLevel": 16
    },
    {
        "latitude": 44.2456674,
        "longitude": 28.266992,
        "title": "BCR Medgidia",
        "description": "Strada Republicii nr.51, Medgidia, Constanta",
        "zoomLevel": 16
    },
    {
        "latitude": 44.1798341,
        "longitude": 28.5886559,
        "title": "BCR Palas",
        "description": "Strada I.C.Bratianu nr.98 Bl.SR3, Constanta, Constanta",
        "zoomLevel": 16
    },
    {
        "latitude": 44.1687543,
        "longitude": 28.6332991,
        "title": "BCR Constanta",
        "description": "Strada Traian nr.68, Constanta, Constanta",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.2029003,
        "longitude": 28.6433326,
        "title": "BCR Mamaia",
        "description": "Bulevardul Mamaia nr.231, Constanta, Constanta",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.0053592,
        "longitude": 28.3295376,
        "title": "BCR Mangalia",
        "description": "Soseaua Constanta nr.25, Mangalia, Constanta",
        "zoomLevel": 16
    },
    {
        "latitude": 44.3210393,
        "longitude": 28.604052,
        "title": "BCR Navodari",
        "description": "Strada Albinelor nr.9 Bl.B2 sc.A parter, Navodari, Constanta",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.2513685,
        "longitude": 27.9387377,
        "title": "BCR Panait Istrati",
        "description": "Soseaua Buzaului bloc B1 parter, Braila, Braila",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.1542525,
        "longitude": 26.8180219,
        "title": "BCR Buzau",
        "description": "Strada Unirii nr.207, Buzau, Buzau",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.154271,
        "longitude": 26.8114558,
        "title": "BCR Ramnicu Sarat",
        "description": "Strada T.Vladimirescu nr.10, Ramnicu Sarat, Buzau",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.429626,
        "longitude": 28.0399307,
        "title": "BCR Galati",
        "description": "Strada Brailei Nr.88, Bl.BR5B, parter, Galati, Galati",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.4308989,
        "longitude": 28.0574322,
        "title": "BCR Port",
        "description": "Strada Portului nr.25 Bl. Siret 4 Sc.9 parter, Galati, Galati",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.84718418079525, 
        "longitude": 27.42998076853861,
        "title": "BCR Tecuci",
        "description": "Strada 1 Decembrie 1918 nr.55, Tecuci, Galati",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.4430043,
        "longitude": 28.0446076,
        "title": "BCR Traian",
        "description": "Strada Traian Bl.A9 parter, Galati, Galati",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.4430228,
        "longitude": 28.0380415,
        "title": "BCR Barlad",
        "description": "Strada Republicii nr. 252, Barlad, Vaslui",
        "zoomLevel": 16
    },
    {
        "latitude": 46.6720402,
        "longitude": 28.0586764,
        "title": "BCR Husi",
        "description": "Strada Al.I.Cuza nr. 3, Husi, Vaslui",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.8359983,
        "longitude": 27.4534252,
        "title": "BCR Negresti",
        "description": "Strada Unirii nr. 1 B, Negresti, Vaslui",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.6364921,
        "longitude": 27.7300334,
        "title": "BCR Vaslui",
        "description": "Strada Stefan cel Mare nr. 53, Vaslui, Vaslui",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.7319609,
        "longitude": 27.4579507,
        "title": "BCR Campina",
        "description": "Bulevardul Carol I nr. 31, Campina, Prahova",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.6938369,
        "longitude": 25.755498,
        "title": "BCR Partizani",
        "description": "Soseaua Nordului, nr.1 parter, Ploiesti, Prahova",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.9375683,
        "longitude": 25.9993495,
        "title": "BCR Cantacuzino",
        "description": "Strada Ghe. Gr. Cantacuzino nr. 193, Ploiesti, Prahova",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.9317631,
        "longitude": 26.0063699,
        "title": "BCR Ploiesti Sud",
        "description": "Strada Mihai Eminescu nr. 28 A, Ploiesti, Prahova",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.1872064,
        "longitude": 26.0374428,
        "title": "BCR Valenii de Munte",
        "description": "Strada Berevoiesti nr. 6, Valenii de Munte, Prahova",
        "zoomLevel": 16
    },
    {
        "latitude": 44.9410434,
        "longitude": 26.0201441,
        "title": "BCR Prahova",
        "description": "Piata Victoriei nr. 1, Ploiesti, Prahova, Ploiesti, Prahova",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.941062,
        "longitude": 26.013578,
        "title": "BCR Arges",
        "description": "Strada Republicii nr.83, Pitesti, Arges",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.8524589,
        "longitude": 24.8678111,
        "title": "BCR Exercitiu",
        "description": "Strada Exercitiu bloc.D15, Pitesti, Arges",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.8696344,
        "longitude": 24.8484726,
        "title": "BCR Pitesti",
        "description": "Strada Mircea Eliade nr.10, Pitesti, Arges",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.8696672,
        "longitude": 24.8331517,
        "title": "BCR Campulung Muscel",
        "description": "Strada Istrate Rizeanu nr.4, Campulung, Arges",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.8697254,
        "longitude": 24.8331517,
        "title": "BCR Curtea de Arges",
        "description": "Bulevardul Basarabilor nr.97, Curtea de Arges, Arges",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.9593905,
        "longitude": 24.940157,
        "title": "BCR Dacia",
        "description": "Bulevardul Dacia Bl L10. Parter, Mioveni, Arges",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.1114083,
        "longitude": 24.988347,
        "title": "BCR Rosiorii de Vede",
        "description": "Strada Rahovei nr. 106, Rosiorii de Vede, Teleorman",
        "zoomLevel": 16 
    },
    {
        "latitude": 43.9710134,
        "longitude": 25.3222437,
        "title": "BCR Teleorman",
        "description": "Strada Dunarii nr. 137, Alexandria, Teleorman",
        "zoomLevel": 16 
    },
    {
        "latitude": 43.9710468,
        "longitude": 25.3069228,
        "title": "BCR Turnu Magurele", 
        "description": "Strada Gen. David Praporgescu Bl. G6 parter, Turnu Magurele, Teleorman",
        "zoomLevel": 16 
    },
    {
        "latitude": 43.9711059,
        "longitude": 25.3069228,
        "title": "BCR Gaesti",
        "description": "Strada 13 Decembrie nr.62, Gaesti, Dambovita",
        "zoomLevel": 16 
    },
    {
        "latitude": 43.971165,
        "longitude": 25.3069228,
        "title": "BCR Moreni",
        "description": "Strada Cpt.Pantea Ion nr.62, Moreni, Dambovita",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.0769414,
        "longitude": 25.4291883,
        "title": "BCR Pucioasa",
        "description": "Strada Republicii nr.105, Pucioasa, Dambovita",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.6603915,
        "longitude": 25.5672218,
        "title": "BCR Titu",
        "description": "Strada I.C.Visarion nr.8, Titu, Dambovita",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.4461176,
        "longitude": 25.7577947,
        "title": "BCR Bolintin Vale",
        "description": "Strada Republicii Bl.B5 Sc.A parter, Con. Bolintin Vale, Giurgiu",
        "zoomLevel": 16 
    },
    {
        "latitude": 43.9026179,
        "longitude": 25.9542906,
        "title": "BCR Giurgiu",
        "description": "Strada Vlad ??epes nr.14 Bl. MUV 3, Giurgiu, Giurgiu",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.037529,
        "longitude": 23.2701724,
        "title": "BCR Gorj", 
        "description": "Strada Geneva nr.2, Targu Jiu, Gorj",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.804018, 
        "longitude":  22.9674435,
        "title": "BCR Motru",
        "description": "Bulevardul Trandafirilor nr. 7C parter, Motru, Gorj",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.9036245,
        "longitude": 23.1381106,
        "title": "BCR Rovinari",
        "description": "Strada Minerilor nr.9 Bl.L1 parter, Rovinari, Gorj",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.026329318626225, 
        "longitude": 23.267919691026318,
        "title": "BCR Victoria Gorj",
        "description": "Strada Victoriei Bl. 194 parter, Targu Jiu, Gorj",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.3171927,
        "longitude": 23.7937451,
        "title": "BCR Dolj",
        "description": "Strada Olte?? nr.4, Craiova, Dolj",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.5547348,
        "longitude": 23.5155001,
        "title": "BCR Filiasi",
        "description": "Bulevardul Racoteanu nr.162 Bl. I 2 parter si Str.Stadionului Bl. I 1 parter, Filiasi, Dolj",
        "zoomLevel": 16 
    },
    { 
        "latitude": 44.5117084,
        "longitude": 22.7336183,
        "title": "BCR Calafat", 
        "description": "Strada Tudor Vladimirescu nr.26, Calafat, Dolj",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.6254543,
        "longitude": 22.6493141,
        "title": "BCR Mehedinti",
        "description": "Strada Aurelian nr. 44, Drobeta Turnu Severin, Mehedinti",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.7240408,
        "longitude": 22.3942738,
        "title": "BCR Orsova",
        "description": "Bulevardul Portile de Fier, nr. 3, Orsova, judet Mehedinti, Orsova, Mehedinti",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.34570046050171, 
        "longitude": 24.118090886468345,
        "title": "BCR Bals",
        "description": "Strada N.Balcescu nr. 186 A, Bals, Olt",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.10433,
        "longitude": 24.3627548,
        "title": "BCR Valcea",
        "description": "Strada Gen. Magheru nr. 20, Ramnicu Valcea, Valcea",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.6603146,
        "longitude": 24.262822,
        "title": "BCR Dragasani",
        "description": "Strada Decebal nr. 2 Bl. G, Dragasani, Valcea",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.9008079,
        "longitude": 23.8475063,
        "title": "BCR Horezu",
        "description": "Strada Tudor Vladimirescu nr. 83 Bl. R2 parter, Horezu, Valcea",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.9010957,
        "longitude": 23.8475039,
        "title": "BCR Arad",
        "description": "Strada Nelu Aristide Dragomir nr.14-16, Arad, Arad",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.17186075955086,
        "longitude":  21.316231529928103,
        "title": "BCR Avram Iancu",
        "description": "Bulevardul Revolutiei nr. 97 parter, Arad, Arad",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.4256275,
        "longitude": 21.8375376,
        "title": "BCR Ineu",
        "description": "Strada Republicii nr.40, Ineu, Arad",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.6680025,
        "longitude":22.3464314,
        "title": "BCR Beius",
        "description": "Strada Samuil Vulcan nr.11, Beius, Bihor",
        "zoomLevel": 16 
    },
    {
        "latitude": 47.0497327,
        "longitude": 21.9367585,
        "title": "BCR Bihor",
        "description": "Strada D.Cantemir nr.2/c, Oradea, Bihor",
        "zoomLevel": 16 
    },
    {
        "latitude": 47.2593711,
        "longitude": 23.2540946,
        "title": "BCR Jibou",
        "description": "Strada 1 Mai nr. 21/A, Jibou, Salaj",
        "zoomLevel": 16 
    },
    {
        "latitude": 47.6835816,
        "longitude": 22.4724113,
        "title": "BCR Carei",
        "description": "Strada Dr.Stefan Vonhaz nr. 2, Carei, Satu Mare",
        "zoomLevel": 16 
    },
    {
        "latitude": 47.8714707,
        "longitude": 23.4251261,
        "title": "BCR Negresti Oas",
        "description": "Strada Victoriei nr. 134, Negresti Oas, Satu Mare",
        "zoomLevel": 16 
    },
    {
        "latitude": 47.7943272,
        "longitude": 22.8748931,
        "title": "BCR Satu Mare",
        "description": "Strada Horea, nr 8-10, Satu-Mare, Satu Mare, Satu Mare",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.7653895,
        "longitude": 21.2228593,
        "title": "BCR Timis",
        "description": "Calea Aradului nr. 11, Timisoara, Timis",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.6099551,
        "longitude": 22.9469379,
        "title": "BCR Hateg",
        "description": "Strada Unirii Bl.48 parter, Hateg, Hunedoara",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.5016267,
        "longitude": 23.0261756,
        "title": "BCR Petrosani",
        "description": "Strada Mihai Viteazu nr.4, Petrosani, Hunedoara",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.5019368,
        "longitude": 23.026175,
        "title": "BCR Brad",
        "description": "Strada Republicii nr.3, Brad, Hunedoara",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.8777603,
        "longitude": 22.9023212,
        "title": "BCR Deva",
        "description": "Str. Maresal Averescu, nr 7, Deva, Judetul Hunedoara, Deva, Hunedoara",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.7540817,
        "longitude": 22.9013349,
        "title": "BCR Hunedoara",
        "description": "Str. George Enescu, nr. 6, Hunedoara, Hunedoara",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.8387538,
        "longitude": 23.1896395,
        "title": "BCR Orastie",
        "description": "Bulevardul Eroilor Bl. B1, Orastie, Hunedoara",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.4101312,
        "longitude": 22.2168307,
        "title": "BCR Caransebes",
        "description": "Strada Mihai Viteazu nr.44, Caransebes, Caras-Severin",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.28815206460043, 
        "longitude": 21.885373924495678,
        "title": "BCR Resita",
        "description": "Strada I.L.Caragiale nr.10, Resita, Caras-Severin",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.7520499,
        "longitude": 21.2225549,
        "title": "BCR Piata Operei", 
        "description": "Strada Piata Victoriei, nr.8, Timisoara, Timis",
        "zoomLevel": 16
    },
    {
        "latitude": 45.7278192,
        "longitude": 21.1991839,
        "title": "BCR Calea Sagului",
        "description": "Calea Sagului nr. 70 Sc. A parter, Timisoara, Timis",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.162586,
        "longitude": 24.3461817,
        "title": "BCR Medias",
        "description": "Strada Mihai Eminescu nr .2 A, Medias, Sibiu",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.795746,
        "longitude": 24.1490428,
        "title": "BCR Nicolae Balcescu",
        "description": "Strada Piata Mare nr. 7, Sibiu, Sibiu, Sibiu",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.782586064470195, 
        "longitude": 24.148857738006903,
        "title": "BCR Aurel Vlaicu",
        "description": "Bulevardul Mihai Viteazu nr. 1 Bl. V 3, Sibiu, Sibiu",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.7896531,
        "longitude": 24.1424518,
        "title": "BCR Sibiu",
        "description": "Strada Emil Cioran nr. 1, Sibiu, Sibiu",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.7010569,
        "longitude": 25.4456255,
        "title": "BCR Codlea", 
        "description": "Strada Lunga nr.125, Codlea, Brasov",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.84357305245107, 
        "longitude": 24.969826620675864,
        "title": "BCR Fagaras",
        "description": "Bulevardul Unirii 2B, Fagaras, Brasov",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.7299802,
        "longitude": 24.6985641,
        "title": "BCR Victoria Brasov", 
        "description": "Strada 1 Decembrie 1918 nr.2, Victoria, Brasov",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.7299802,
        "longitude": 24.6962681,
        "title": "BCR Brasov",
        "description": "AFI Brasov, Blvd. 15 Noiembrie, nr. 78, etaj 2, Brasov, Brasov",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.0758574,
        "longitude": 25.5959692,
        "title": "BCR Baraolt",
        "description": "Strada Libertatii 2/A, Baraolt, Covasna",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.8636024,
        "longitude": 25.7888341,
        "title": "BCR Covasna",
        "description": "Strada Jozef Bem nr. 7, Sfantu Gheorghe, Covasna",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.6745812,
        "longitude": 26.0307271,
        "title": "BCR Intorsura Buzaului",
        "description": "Strada Mihai Viteazu Nr. 143 Bl. 6 Sc .C, Intorsura Buzaului, Covasna",
        "zoomLevel": 16 
    },
    { 
        "latitude": 45.9833552,
        "longitude": 25.2602758,
        "title": "BCR Targu Secuiesc",
        "description": "Strada Piata Gabor Aron nr.17, Targu Secuiesc, Covasna",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.47126007308539, 
        "longitude": 24.095459255229347,
        "title": "BCR Ludus",
        "description": "Bulevardul 1 Decembrie nr. 43/B parter, Ludus, Mures",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.5392994,
        "longitude": 24.5541824,
        "title": "BCR Mures",
        "description": "Strada Gh.Doja nr. 1-3, Targu Mures, Mures",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.4369612,
        "longitude": 24.2813651,
        "title": "BCR Tarnaveni",
        "description": "Piata Trandafirilor nr. 16, Tarnaveni, Mures",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.541621,
        "longitude": 24.5546033,
        "title": "BCR Central",
        "description": "Piata Trandafirilor nr.26, Targu Mures, Mures",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.5416565,
        "longitude": 24.541471,
        "title": "BCR Reghin",
        "description": "Piata Petru Maior, nr. 43, Reghin, Mures",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.2153773,
        "longitude": 24.7879188,
        "title": "BCR Sighisoara",
        "description": "Strada 1 Mai nr. 12, Sighisoara, Mures",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.1416936,
        "longitude": 23.9775478,
        "title": "BCR Tudor",
        "description": "Bulevardul 1 Decembrie 1918 nr. 180, Targu Mures, Mures",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.2895061,
        "longitude": 25.0327024,
        "title": "BCR Cristuru Secuiesc",
        "description": "Strada Libertatii nr.44, Cristuru Secuiesc, Harghita",
        "zoomLevel": 16 
    },
    {
        "latitude":46.723068050340025, 
        "longitude": 25.596981156701844,
        "title": "BCR Gheorgheni",
        "description": "Str. Nicolae Balcescu, nr. 7, parter, Gheorgheni, Harghita",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.3629039,
        "longitude": 25.8015872,
        "title": "BCR Harghita",
        "description": "Strada Kossuth Lajos nr.2, Miercurea Ciuc, Harghita",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.3018492,
        "longitude": 25.2866504,
        "title": "BCR Odorheiu Secuiesc",
        "description": "Strada Piata Libertatii nr.15, Odorheiu Secuiesc, Harghita",
        "zoomLevel": 16 
    },
    {
        "latitude": 46.922924,
        "longitude": 25.3490098,
        "title": "BCR Toplita",
        "description": "Strada N.Balcescu Bl.C parter, Toplita, Harghita",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.638951,
        "longitude": 25.6285752,
        "title": "BCR",
        "description": "Calea Bucuresti nr.90, Brasov, Brasov",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.5908206,
        "longitude": 25.4628436,
        "title": "BCR Rasnov",
        "description": "Piata Unirii nr.10, Rasnov, Brasov",
        "zoomLevel": 16 
    },
    {
        "latitude": 45.5650372,
        "longitude": 25.3192332,
        "title": "BCR Zarnesti",
        "description": "Strada Mitropolit I.Metianu nr.8, Zarnesti, Brasov",
        "zoomLevel": 16 
    },
    {
        "latitude":44.4120953,
        "longitude": 25.9771565,
        "title": "BCR Ghencea",
        "description": "Strada Brasov nr. 25 sector 6, Bucuresti, Sector 6",
        "zoomLevel": 16 
    },
    {
        "latitude":44.4274631,
        "longitude": 26.1002851,
        "title": "BCR Unirea",
        "description": "Bulevardul Unirii nr.43-45 bl.E2-E3, Bucuresti, Sector 3",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.3807386,
        "longitude": 26.1312313,
        "title": "BCR Berceni", 
        "description": "Strada Ion Iriceanu nr.20-22 bl.131-132, Bucuresti, Sector 4",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.3882343,
        "longitude": 26.115209,
        "title": "BCR Dr. Obregia", 
        "description": "Strada Dr.Al.Obregia nr.2B bl.2B parter, Bucuresti, Sector 4",
        "zoomLevel": 16 
    },
    {
        "latitude":44.4365674,
        "longitude": 26.0973055,
        "title": "BCR Universitate",
        "description": "Calea Victoriei nr. 46, Bucuresti, Sector 1",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.420114,
        "longitude": 26.0175857,
        "title": "BCR Sector 5",
        "description": "Bulevardul Tudor Vladimirescu nr.57 bl. T4, Bucuresti, Sector 5",
        "zoomLevel": 16 
    },
    {
        "latitude":44.4446845,
        "longitude": 26.1204573,
        "title": "BCR Mosilor",
        "description": "Calea Mosilor nr.290 bl.36, Bucuresti, Sector 2",
        "zoomLevel": 16 
    },
    {
        "latitude":44.4518732,
        "longitude": 26.1168334,
        "title": "BCR Stefan cel Mare",
        "description": "Soseaua St.cel Mare nr.60 bl.41 parter, Bucuresti, Sector 2",
        "zoomLevel": 16 
    },
    {
        "latitude":44.4424911,
        "longitude": 26.1661504,
        "title": "BCR Pantelimon",
        "description": "Soseaua Pantelimon nr.291 bl 9 parter, Bucuresti, Sector 2",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.4520615,
        "longitude": 26.127926,
        "title": "BCR Veranda",
        "description": "Strada Ziduri Mosi nr.23, sector 2, Bucuresti, Bucuresti, Sector 2",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.486338,
        "longitude": 26.1791803,
        "title": "BCR Voluntari",
        "description": "Soseaua Bucuresti Afumati nr.52, Voluntari, Ilfov",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.4321195,
        "longitude": 26.1332634,
        "title": "BCR Sector 3",
        "description": "Soseaua Mihai Bravu nr.196 bl.200, Bucuresti, Sector 2",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.4263403,
        "longitude": 26.1201101,
        "title": "BCR Sector 4",
        "description": "Bulevardul Unirii nr.63 bl.F4, Bucuresti, Sector 3",
        "zoomLevel": 16 
    },
    {
        "latitude":44.4120495,
        "longitude": 26.1693239,
        "title": "BCR Th. Pallady",
        "description": "Bulevardul Th. Pallady nr.7-9 bl.R5, Bucuresti, Sector 3",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.4307369,
        "longitude": 26.05185,
        "title": "BCR AFI",
        "description": "Bulevardul Vasile Milea, nr. 4E, sector 6, cladirea AFI Park 1, Bucuresti, Sector 6",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.4513035,
        "longitude": 26.0842568,
        "title": "BCR Sector 1",
        "description": "Calea Victoriei nr.155 bl.D1 sector 1, Bucuresti, Sector 1",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.4966535,
        "longitude": 26.0282765,
        "title": "BCR Bucurestii Noi" ,
        "description": "Bulevardul Bucurestii Noi nr.170, Bucuresti, Sector 1",
        "zoomLevel": 16 
    },
    {
        "latitude": 44.4967132,
        "longitude": 25.9954456,
        "title": "BCR Otopeni",
        "description": "Calea Bucuresti nr.82 bl.B2-2 parter jud. Ilfov, Otopeni, Ilfov",
        "zoomLevel": 16 
    }
    ]
    ##get location-data.json from static
    return jsonify(STOREA_DATA)
  
@app.route("/map",methods=["GET"])
def map_get():
    return render_template("index.html")

@app.route("/map_second",methods=["GET"])
def map_get_second():
    return render_template("map_carmen_index.html")


@app.route("/dashboard",methods=["GET"])
def dashboard():
    return render_template("dashboard.html")

@app.route("/dashboard_map",methods=["GET"])
def dashboard_map():
    return render_template("dashboard_map.html")

@app.route("/dashboard_plots",methods=["GET"])
def dashboard_plots():
    return render_template("dashboard_plots.html")

@app.route("/sucursale",methods=["GET"])
def sucursale():
    return render_template("sucursale.html")

@app.route("/index",methods=["GET"])
def index_first_page():
    return render_template("index_mar.html")

@app.route("/main",methods=["GET"])
def main_page():
    return render_template("main.html")

@app.route("/chatbot",methods=["GET"])
def chatbot():
    return render_template("chatbot.html")

@app.route("/chatbot_responses",methods=["GET"])
def chatbot_responses():
   
    query = request.args.get("message") 
   
    let_data = [["how I create an appointment?",
        "Go to the home page and click on the schedule programati intalnirea."],
        ["how do I make an appointment in a branch?",
    "Go to the home page and click on the schedule programati intalnirea."],
    ["How I can create a credit bcr?",
    "We provide you with a fast online loan to make your wishes come true. Set up your credit with just a few taps on the screen and receive the loan online. You simply and quickly choose the amount you want to borrow and the crediting period."],
        ["How many clients do you have ?",
    "At the moment we have 3.1 million customers, 7,237 employees and 509 branches."]]
    add=[]
    for i in let_data:
        if i[0].find(query)!=-1:
            add.append(i[1])
   
    
    exit_conditions = (":q", "quit", "exit")

    if query in exit_conditions:
        return {"data":"error"}
    else:
        return {"data":add}
           

if __name__ == '__main__':
    app.run(host='0.0.0.0')