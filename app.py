#####################################################################
# IMPORTATION DES MODULES
#####################################################################

from flask import Flask, render_template, request
import matplotlib
import basededonnee.db as db
import pandas as pd
import math
from flask import send_from_directory


#####################################################################
# CONFIGURATION
#####################################################################

# Déclaration d'application Flask
app = Flask(__name__)

# Assure la compatibilité de Matplotlib avec Flask
matplotlib.use('Agg')

#####################################################################
# CONTROLEUR : ROUTES VERS LES VUES
#####################################################################


@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory('media', filename)


# Route pour la page d'accueil
@app.route('/')
def accueil():
    # Affichage du template
    return render_template('index.html')

# Route pour la page d'à propos
@app.route('/apropos')
def apropos():
    # Affichage du template
    return render_template('apropos.html')


@app.route('/graphes')
def graphes():
    return render_template('graphe.html')


# Route pour afficher le contenu de la table "category"
@app.route('/ildefrance', methods=['GET'])
def afficher_idf():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Ile-de-France")
        data = db.get_data_by_region("Ile-de-France", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Ile-de-France")
        data = db.get_data_by_region("Ile-de-France", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Ile-de-France")
        data = db.get_data_by_region("Ile-de-France", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'iledefrance.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )






###################################################################""








@app.route('/guadeloupe', methods=['GET'])
def afficher_guadeloupe():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Guadeloupe")
        data = db.get_data_by_region("Guadeloupe", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Guadeloupe")
        data = db.get_data_by_region("Guadeloupe", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Guadeloupe")
        data = db.get_data_by_region("Guadeloupe", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'guadeloupe.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    
    
####################################################################################

@app.route('/martinique', methods=['GET'])
def afficher_martinique():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Martinique")
        data = db.get_data_by_region("Martinique", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Martinique")
        data = db.get_data_by_region("Martinique", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Martinique")
        data = db.get_data_by_region("Martinique", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'martinique.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    

#########################################################################




@app.route('/guyane', methods=['GET'])
def afficher_guyane():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Guyane")
        data = db.get_data_by_region("Guyane", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Guyane")
        data = db.get_data_by_region("Guyane", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Guyane")
        data = db.get_data_by_region("Guyane", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'guyane.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
   
   
#####################################################################   
    
    
@app.route('/reunion', methods=['GET'])
def afficher_reunion():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("La Réunion")
        data = db.get_data_by_region("La Réunion", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("La Réunion")
        data = db.get_data_by_region("La Réunion", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("La Réunion")
        data = db.get_data_by_region("La Réunion", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'reunion.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    
    
    
#############################################################################

@app.route('/mayotte', methods=['GET'])
def afficher_mayotte():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Mayotte")
        data = db.get_data_by_region("Mayotte", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Mayotte")
        data = db.get_data_by_region("Mayotte", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Mayotte")
        data = db.get_data_by_region("Mayotte", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'mayotte.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    
    
    
    
##############################################

@app.route('/centrevaldeloire', methods=['GET'])
def afficher_centrevaldeloire():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Centre-Val de Loire")
        data = db.get_data_by_region("Centre-Val de Loire", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Mayotte")
        data = db.get_data_by_region("Centre-Val de Loire", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("    ")
        data = db.get_data_by_region("Centre-Val de Loire", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'centrevaldeloire.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    
###################################
@app.route('/bourgognefranchecomte', methods=['GET'])
def afficher_bourgognefranchecomte():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Bourgogne-Franche-Comté")
        data = db.get_data_by_region("Bourgogne-Franche-Comté", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Bourgogne-Franche-Comté")
        data = db.get_data_by_region("Bourgogne-Franche-Comté", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Bourgogne-Franche-Comté")
        data = db.get_data_by_region("Bourgogne-Franche-Comté", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'bourgognefranchecomte.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    
    
    
##########################################################







@app.route('/normandie', methods=['GET'])
def afficher_normandie():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Normandie")
        data = db.get_data_by_region("Normandie", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Normandie")
        data = db.get_data_by_region("Normandie", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Normandie")
        data = db.get_data_by_region("Normandie", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'normandie.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
  
  
  
  
    
##############################################################





@app.route('/hautsdefrance', methods=['GET'])
def afficher_hautsdefrance():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Hauts-de-France")
        data = db.get_data_by_region("Hauts-de-France", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Hauts-de-France")
        data = db.get_data_by_region("Hauts-de-France", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Hauts-de-France")
        data = db.get_data_by_region("Hauts-de-France", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'hautsdefrance.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    
##########################################################


@app.route('/grandest', methods=['GET'])
def afficher_grandest():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Grand Est")
        data = db.get_data_by_region("Grand Est", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Grand Est")
        data = db.get_data_by_region("Grand Est", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Grand Est")
        data = db.get_data_by_region("Grand Est", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'grandest.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    
    

###################################################

@app.route('/paysdelaloire', methods=['GET'])
def afficher_paysdelaloire():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Pays de la Loire")
        data = db.get_data_by_region("Pays de la Loire", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Pays de la Loire")
        data = db.get_data_by_region("Pays de la Loire", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Pays de la Loire")
        data = db.get_data_by_region("Pays de la Loire", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'paysdelaloire.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    

#################################

@app.route('/bretagne', methods=['GET'])
def afficher_bretagne():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Bretagne")
        data = db.get_data_by_region("Bretagne", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Bretagne")
        data = db.get_data_by_region("Bretagne", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Bretagne")
        data = db.get_data_by_region("Bretagne", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'bretagne.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    
    
##################################


@app.route('/nouvelleaquitaine', methods=['GET'])
def afficher_nouvelleaquitaine():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Nouvelle-Aquitaine")
        data = db.get_data_by_region("Nouvelle-Aquitaine", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Nouvelle-Aquitaine")
        data = db.get_data_by_region("Nouvelle-Aquitaine", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Nouvelle-Aquitaine")
        data = db.get_data_by_region("Nouvelle-Aquitaine", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'nouvelleaquitaine.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    

############################################

@app.route('/occitanie', methods=['GET'])
def afficher_occitanie():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Occitanie")
        data = db.get_data_by_region("Occitanie", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Occitanie")
        data = db.get_data_by_region("Occitanie", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Occitanie")
        data = db.get_data_by_region("Occitanie", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'occitanie.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    
    
    
##############################

@app.route('/auvergnerhonesalpes', methods=['GET'])
def afficher_auvergnerhonesalpes():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Auvergne-Rhône-Alpes")
        data = db.get_data_by_region("Auvergne-Rhône-Alpes", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Auvergne-Rhône-Alpes")
        data = db.get_data_by_region("Auvergne-Rhône-Alpes", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Auvergne-Rhône-Alpes")
        data = db.get_data_by_region("Auvergne-Rhône-Alpes", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'auvergnerhonesalpes.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    
    
    
#######################################

@app.route('/provencesalpescote', methods=['GET'])
def afficher_provencesalpescote():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Provence-Alpes-Côte d\'Azur")
        data = db.get_data_by_region("Provence-Alpes-Côte d\'Azur", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Provence-Alpes-Côte d\'Azur")
        data = db.get_data_by_region("Provence-Alpes-Côte d\'Azur", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Provence-Alpes-Côte d\'Azur")
        data = db.get_data_by_region("Provence-Alpes-Côte d\'Azur", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'provencesalpescote.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    
    
##################################

@app.route('/corse', methods=['GET'])
def afficher_corse():
    # Récupérer le tableau sélectionné
    tableau = request.args.get("tableau", "Demographie")

    # Pagination
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    # Charger les données selon le tableau sélectionné
    if tableau == "Demographie":
        total_count = db.TotalDemographie("Corse")
        data = db.get_data_by_region("Corse", "demographie", limit=limit, offset=offset)
    elif tableau == "Honoraires":
        total_count = db.TotalHonoraires("Corse")
        data = db.get_data_by_region("Corse", "honoraires", limit=limit, offset=offset)
    elif tableau == "Prescriptions":
        total_count = db.TotalPrescription("Corse")
        data = db.get_data_by_region("Corse", "prescription", limit=limit, offset=offset)
    else:
        total_count = 0
        data = pd.DataFrame()

    # Calcul du nombre total de pages
    total_pages = math.ceil(total_count / limit)
    pages = list(range(max(1, page - 2), min(total_pages + 1, page + 3)))

    # Retourner le template
    return render_template(
        'corse.html',
        tableau=tableau,
        data=data,
        page=page,
        total_pages=total_pages,
        pages=pages
    )
    
    
    
    
    
    

    
    
    
    

    
    
    
    
    
    
    
    
    
    


 
#####################################################################
# POINT D'ENTREE DU PROGRAMME
#####################################################################

if __name__ == '__main__':
    app.run(debug=True)
