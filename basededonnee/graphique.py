import os
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Nom de la base de données SQLite
DATABASE = "sae_104"

# Chemin relatif vers la base de données
db_path = os.path.join(os.path.dirname(__file__), 'data', DATABASE)


# Fonction pour se connecter à la base de données
def connect_db():
    # Connection à la base
    return sqlite3.connect(db_path)

####################################################################


####################################################################

# Requête SQL pour récupérer les données par prescription par region 
query = """
   SELECT 
    r.Region_nom, 
    SUM(p.montant_total_prescription) AS Prescriptions
FROM Prescription p
JOIN Profession_sante ps ON p.Profession_id = ps.Profession_id
JOIN Demographie d ON ps.Profession_id = d.Profession_id
JOIN Departement dep ON d.Departement_id = dep.Departement_id
JOIN Regions r ON dep.Region_id = r.Region_id
GROUP BY r.Region_nom
ORDER BY Prescriptions DESC;

"""
# Exécution de la requête et récupération des données
conn = connect_db()
df_prescription = pd.read_sql_query(query, conn)
conn.close()



# Vérification des données, pas obligatoire mais cool pour comparer si ya une erreur
print(df_prescription.head())  # Montre les 5 premières lignes
print(df_prescription.columns)  # Affichez les colonnes pour valider leurs noms



# creation du graphique
plt.figure(figsize=(12, 6))
plt.bar(df_prescription['Region_nom'], df_prescription['Prescriptions'], color='skyblue')
plt.title("Somme des prescriptions total par region (en €)", fontsize=16)
plt.xlabel("Region", fontsize=12)
plt.ylabel("Prescriptions en €", fontsize=12)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()