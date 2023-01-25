import mysql.connector
from flask import Flask, request

app = Flask(__name__)

# Connexion à la base de données
cnx = mysql.connector.connect(user='username', password='password',
                              host='hostname', database='database_name')
cursor = cnx.cursor()

@app.route('/get_quote', methods=['POST'])
def get_quote():
    # Récupération des données du formulaire
    data = request.form
    make = data['make']
    model = data['model']
    year = data['year']

    # Exécution de la requête SQL pour récupérer les informations de l'assurance
    query = "SELECT price FROM car_insurance WHERE make = '{}' AND model = '{}' AND year = '{}'".format(make, model, year)
    cursor.execute(query)
    result = cursor.fetchone()

    # Retourne le prix de l'assurance
    return str(result[0])

if __name__ == '__main__':
    app.run(debug=True)
