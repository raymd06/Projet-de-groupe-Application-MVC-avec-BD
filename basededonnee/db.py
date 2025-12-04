import os
import pandas as pd
import sqlite3

# Nom de la base de données SQLite
DATABASE = "sae_104"
db_path = os.path.join(os.path.dirname(__file__), 'data', DATABASE)

def connect_db():
    return sqlite3.connect(db_path)

def get_data_by_region(region_name, table_type, limit=5, offset=0):
    conn = connect_db()

    queries = {
        "honoraires": f"""
            SELECT Profession_nom, annee, Honoraires_ordre_niv_1, type_honoraires_niveau_1, 
                   Honoraires_ordre_niv_2, type_honoraires_niveau_2, Honoraires_ordre_niv_3, 
                   type_honoraires_niveau_3, Montant_des_honoraires, Montant_des_honoraires_moyens
            FROM Honoraires h
            JOIN Profession_sante ps ON h.Profession_id = ps.Profession_id
            JOIN Demographie d ON ps.Profession_id = d.Profession_id
            JOIN Departement dep ON d.Departement_id = dep.Departement_id
            JOIN Regions r ON dep.Region_id = r.Region_id
            WHERE r.Region_nom = "{region_name}"
            LIMIT {limit} OFFSET {offset};
        """,
        "demographie": f"""
            SELECT Profession_nom, Departement_nom, type_exercice_liberal, profession_effectif
            FROM Demographie d
            JOIN Profession_sante ps ON ps.Profession_id = d.Profession_id
            JOIN Departement dep ON d.Departement_id = dep.Departement_id
            JOIN Regions r ON dep.Region_id = r.Region_id
            WHERE r.Region_nom = "{region_name}"
            LIMIT {limit} OFFSET {offset};
        """,
        "prescription": f"""
            SELECT Profession_nom, annee, poste_prescription_nom, 
                   montant_total_prescription, montant_moyen_prescription
            FROM Prescription p
            JOIN Profession_sante ps ON ps.Profession_id = p.Profession_id
            JOIN Demographie d ON p.Profession_id = d.Profession_id
            JOIN Departement dep ON d.Departement_id = dep.Departement_id
            JOIN Regions r ON dep.Region_id = r.Region_id
            WHERE r.Region_nom = "{region_name}"
            LIMIT {limit} OFFSET {offset};
        """
    }

    query = queries.get(table_type)
    if not query:
        raise ValueError("Type de table non valide. Utilisez 'honoraires', 'demographie' ou 'prescription'.")
    
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data



def TotalPrescription(region_name) :
    conn = connect_db()
    query = f"""
        SELECT COUNT(*) AS total
            FROM Prescription p
            JOIN Profession_sante ps ON ps.Profession_id = p.Profession_id
            JOIN Demographie d ON p.Profession_id = d.Profession_id
            JOIN Departement dep ON d.Departement_id = dep.Departement_id
            JOIN Regions r ON dep.Region_id = r.Region_id
            WHERE r.Region_nom = "{region_name}"
        """
    result = pd.read_sql_query(query, conn)
    conn.close()
    return int(result['total'][0])

def TotalDemographie(region_name) :
    conn = connect_db()
    query = f"""
        SELECT COUNT(*) AS total  
            FROM Demographie d
            JOIN Profession_sante ps ON ps.Profession_id = d.Profession_id
            JOIN Departement dep ON d.Departement_id = dep.Departement_id
            JOIN Regions r ON dep.Region_id = r.Region_id
            WHERE r.Region_nom = "{region_name}"
        """
    result = pd.read_sql_query(query, conn)
    conn.close()
    return int(result['total'][0])

def TotalHonoraires(region_name) :
    conn = connect_db()
    query = f"""
        SELECT COUNT(*) AS total FROM Honoraires h 
        JOIN Profession_sante ps ON h.Profession_id = ps.Profession_id
        JOIN Demographie d ON ps.Profession_id = d.Profession_id
        JOIN Departement dep ON d.Departement_id = dep.Departement_id
        JOIN Regions r ON dep.Region_id = r.Region_id
        WHERE r.Region_nom = "{region_name}"
        """
    result = pd.read_sql_query(query, conn)
    conn.close()
    return int(result['total'][0])

