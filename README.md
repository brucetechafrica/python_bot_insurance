# python_bot_insurance

Ce script utilise la bibliothèque Flask pour créer un serveur web et gérer les requêtes HTTP. Il utilise également la bibliothèque MySQL Connector pour se connecter à une base de données MySQL et exécuter des requêtes SQL.

Lorsqu'un utilisateur soumet un formulaire contenant les informations sur le véhicule (marque, modèle, année), la fonction get_quote est appelée. Cette fonction récupère les données du formulaire, construit une requête SQL pour récupérer le prix de l'assurance correspondant au véhicule spécifié, exécute la requête et retourne le prix.

Ce script nécessite que la base de données contient une table nommée "car_insurance" avec des colonnes "make", "model", "year" et "price".
