import pandas as pd
import numpy as np
import pymysql

df = pd.read_csv('./saveBDD.csv', sep=';', decimal=',', quotechar='"')

# supprime id qui va etre auto incrementé
df = df.drop(['id'], axis=1)

# convertir magasin_id en entiers numeric
df['magasin_id'] = pd.to_numeric(df['magasin_id'], errors='coerce').astype('Int64')
# remplace les NaN de magasin_id par une valeur numérique NULL
df['magasin_id'] = df['magasin_id'].replace({pd.NA: None})

# convertir categorie_id en entiers numeric
df['categorie_id'] = pd.to_numeric(df['categorie_id'], errors='coerce').astype('Int64')

# convertir marque_id en entiers numeric
df['marque_id'] = pd.to_numeric(df['marque_id'], errors='coerce').astype('Int64')
# remplace les NaN de marque_id par une valeur numérique NULL
df['marque_id'] = df['marque_id'].replace({pd.NA: None})

# convertir type_saveur_id en entiers numeric
df['type_saveur_id'] = pd.to_numeric(df['type_saveur_id'], errors='coerce').astype('Int64')
# remplace les NaN de type_saveur_id par une valeur numérique NULL
df['type_saveur_id'] = df['type_saveur_id'].replace({pd.NA: None})

# remplace les NaN de description par une valeur NULL
df['description'] = df['description'].replace({pd.NA: None})

# convertir dosage_pg_vg_id en entiers numeric
df['dosage_pg_vg_id'] = pd.to_numeric(df['dosage_pg_vg_id'], errors='coerce').astype('Int64')
# remplace les NaN de dosage_pg_vg_id par une valeur numérique NULL
df['dosage_pg_vg_id'] = df['dosage_pg_vg_id'].replace({pd.NA: None})

# convertir contenance_ml_id en entiers numeric
df['contenance_ml_id'] = pd.to_numeric(df['contenance_ml_id'], errors='coerce').astype('Int64')
# remplace les NaN de contenance_ml_id par une valeur numérique NULL
df['contenance_ml_id'] = df['contenance_ml_id'].replace({pd.NA: None})

# convertir dosage_nicotine_mg_id en entiers numeric
df['dosage_nicotine_mg_id'] = pd.to_numeric(df['dosage_nicotine_mg_id'], errors='coerce').astype('Int64')
# remplace les NaN de dosage_nicotine_mg_id par une valeur numérique NULL
df['dosage_nicotine_mg_id'] = df['dosage_nicotine_mg_id'].replace({pd.NA: None})

# remplace 1 par True, 2 par False et nan par False
df['sel_de_nicotine'] = df['sel_de_nicotine'].replace({1: True, 0: False}).fillna(False)

# convertir qte_stock en entiers numeric
df['qte_stock'] = pd.to_numeric(df['qte_stock'], errors='coerce').astype('Int64')

# convertir statut_produit_id en entiers numeric
df['statut_produit_id'] = pd.to_numeric(df['statut_produit_id'], errors='coerce').astype('Int64')

# convertir statut_reappro_id en entiers numeric
df['statut_reappro_id'] = pd.to_numeric(df['statut_reappro_id'], errors='coerce').astype('Int64')

# créer une colonne id au début remplie de None
df.insert(0, 'id', None)

# Connexion à la base de données MySQL
connection = pymysql.connect(host='localhost',
                             user='theo',
                             password='3630',
                             db='testTeal')

# Créer un curseur pour exécuter des requêtes
cursor = connection.cursor()

# Boucle sur chaque ligne du DataFrame et exécute l'insertion
for _, row in df.iterrows():
    values = (row['id'], row['magasin_id'], row['sku'], row['libelle_produit'], row['libelle_fiche'], row['categorie_id'], row['marque_id'], row['type_saveur_id'], row['description'], row['dosage_pg_vg_id'], row['contenance_ml_id'], row['dosage_nicotine_mg_id'], row['sel_de_nicotine'], row['qte_stock'], row['statut_produit_id'], row['statut_reappro_id'])
    query = "INSERT INTO produits (id, magasin_id, sku, libelle_produit, libelle_fiche, categorie_id, marque_id, type_saveur_id, description, dosage_pg_vg_id, contenance_ml_id, dosage_nicotine_mg_id, sel_de_nicotine, qte_stock, statut_produit_id, statut_reappro_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, values)

# Valider les modifications dans la base de données
connection.commit()

# Fermer la connexion et le curseur
cursor.close()
connection.close()

# save
df.to_csv('./saveBDDAfterScript.csv', sep=';', index=False)