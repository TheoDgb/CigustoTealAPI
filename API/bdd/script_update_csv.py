import pandas as pd
import numpy as np
import pymysql

df = pd.read_csv('./bdd/metabaseFile.csv', sep=',', decimal=',', quotechar='"')

# renommer les colonnes
new_column_names = ['ID', 'sku', 'Code EAN', 'libelle_fiche', 'libelle_produit', 'type produit', 'statut produit centrale', 'categorie_id', 'marque_id', 'gamme', 'description', 'dosage_pg_vg_id', 'dosage_nicotine_mg_id', 'contenance_ml_id', 'sel_de_nicotine', 'type_saveur_id', 'unité vente', 'PA HT centrale (€)', 'PV ttc Conseillé (€)', 'Marge Ht (€)', 'tx marge', 'Pv Ttc Magasin (€)', 'magasin_id', 'qte_stock', 'Ventes Mois M', 'Ventes M 1', 'Ventes M 2', 'statut_produit_id', 'statut_reappro_id']
df.columns = new_column_names

# supprime les colonnes inutiles
df = df.drop(['ID', 'Code EAN', 'type produit', 'statut produit centrale', 'unité vente', 'PA HT centrale (€)', 'PV ttc Conseillé (€)', 'Marge Ht (€)', 'tx marge', 'Pv Ttc Magasin (€)', 'Ventes Mois M', 'Ventes M 1', 'Ventes M 2'], axis=1)

# supprimer les produits doublons
df.drop_duplicates(inplace=True)

# remplace NaN par 0
df['qte_stock'] = df['qte_stock'].fillna(0)
# convertit la colonne Qté stock en entier
df['qte_stock'] = df['qte_stock'].astype(int)

# supprime les lignes qui ne sont pas des liquides / concentrés
df = df[df['categorie_id'].isin(["Liquides 10 ml", "Liquides Grand Format", "Concentrés"])]

# replace NaN par une chaîne vide pour magasin_id
df['magasin_id'] = df['magasin_id'].fillna('')
# 814 fait nimp il est pas considéré comme chaine de carac... ???
df['marque_id'] = df['marque_id'].replace('814', 'delete814')

# remplace "French Liquide" par "Le French Liquide" pour marque_id
df['marque_id'] = df['marque_id'].replace({'French Liquide': 'Le French Liquide'})

# remplace les NaN par une chaîne vide pour description
# df['description'] = df['description'].fillna('')

# remplace les NaN par une chaîne vide pour dosage_pg_vg_id
df['dosage_pg_vg_id'] = df['dosage_pg_vg_id'].fillna('')

# modifie les type_saveur_id "Classic gourmand" en "Classic", "Fruité frais" en "Fruité Frais" et "Boisson" en "Friandise / Boisson"
df['type_saveur_id'] = df['type_saveur_id'].replace({'Classic gourmand': 'Classic', 'Fruité frais': 'Fruité Frais', 'Boisson': 'Friandise / Boisson'})

# supprimer "ml"
df['contenance_ml_id'] = df['contenance_ml_id'].str.replace('ml', '')
 # convertir contenance_ml_id en entiers
df['contenance_ml_id'] = pd.to_numeric(df['contenance_ml_id'], errors='coerce').astype('Int64')

# supprimer "mg"
df['dosage_nicotine_mg_id'] = df['dosage_nicotine_mg_id'].str.replace('mg', '')
 # convertir dosage_nicotine_mg_id en entiers
df['dosage_nicotine_mg_id'] = pd.to_numeric(df['dosage_nicotine_mg_id'], errors='coerce').astype('Int64')

# remplace "oui" par True, vide par False et Non par false
df['sel_de_nicotine'] = df['sel_de_nicotine'].replace({'Oui': True, 'oui': True, 'Non': False, 'non': False}).fillna(False)

# déplacement de certains champs de gamme vers marque_id
mask = df["gamme"] == "Cesar"
df.loc[mask, "marque_id"] = "Cesar"
mask = df["gamme"] == "Devil's"
df.loc[mask, "marque_id"] = "Devil's"
mask = df["gamme"] == "Devil sels de nicotine en Devil's" #erreur de saisie ? o.O
df.loc[mask, "marque_id"] = "Devil's"
mask = df["gamme"] == "Salt-E-vapor"
df.loc[mask, "marque_id"] = "Salt-E-vapor"
mask = df["gamme"] == "Fruizee"
df.loc[mask, "marque_id"] = "Fruizee"
mask = df["gamme"] == "Kung Fruits"
df.loc[mask, "marque_id"] = "Kung Fruits"
mask = df["gamme"] == "Le Coq qui vape"
df.loc[mask, "marque_id"] = "Le Coq qui vape"
mask = df["gamme"] == "Mono+"
df.loc[mask, "marque_id"] = "Mono+"
mask = df["gamme"] == "Enfer"
df.loc[mask, "marque_id"] = "Enfer"

# suppression de la colonne gamme
df.drop('gamme', axis=1)

# réorganise les colonnes
df = df.reindex(columns=['magasin_id', 'sku', 'libelle_produit', 'libelle_fiche', 'categorie_id', 'marque_id', 'type_saveur_id', 'description', 'dosage_pg_vg_id', 'contenance_ml_id', 'dosage_nicotine_mg_id', 'sel_de_nicotine', 'qte_stock', 'statut_produit_id', 'statut_reappro_id'])



# modifie les données pour les insérer dans la bdd
df['magasin_id'] = df['magasin_id'].replace({'CIGUSTO ANDELNANS': 1,
                                             'CIGUSTO BESANCON ECOLE VALENTIN': 2,
                                             'CIGUSTO BESSONCOURT': 3,
                                             'CIGUSTO COLMAR - HOUSSEN': 4
})
# remplace les NaN de magasin_id par une valeur numérique NULL pour pouvoir l'insérer dans une base de données mysql
# df['magasin_id'].replace(np.nan, None, inplace=True)
df['magasin_id'].replace('[^\d]+', None, inplace=True)
df['magasin_id'].replace('', None, inplace=True)

df['categorie_id'] = df['categorie_id'].replace({'Liquides 10 ml': 1,
                                                 'Liquides Grand Format': 2,
                                                 'Concentrés': 3
})
df['marque_id'] = df['marque_id'].replace({'A&L': 1,
                                           'Alfaliquid': 2,
                                           'Bakery Shake': 3,
                                           'Candy Shake': 4,
                                           'Cesar': 5,
                                           'Cigusto': 6,
                                           'Cirkus': 7,
                                           'Curieux': 8,
                                           'Don Cristo': 9,
                                           'Eliquid France': 10,
                                           'Enfer': 11,
                                           'ETasty': 12,
                                           'Fresh Vape Co': 13,
                                           'Fruiteo': 14,
                                           'Fruity Cool': 15,
                                           'Fruity Fuel': 16,
                                           'Fruizee': 17,
                                           'Full Moon': 18,
                                           'Furiosa': 19,
                                           'Greeneo': 20,
                                           'Juicy Shake': 21,
                                           'Kung Fruits': 22,
                                           'Le Coq qui vape': 23,
                                           'Le French Liquide': 24,
                                           'Le Vapoteur Breton': 25,
                                           'Devil\'s': 26,
                                           'Liquideo': 27,
                                           'Mono+': 28,
                                           'Monster': 29,
                                           'Petit Nuage': 30,
                                           'Salt-E-vapor': 31,
                                           'Snap Dragon': 32,
                                           'Swoke': 33,
                                           'The Medusa Juice': 34,
                                           'T-Juice': 35,
                                           'Vampire vape': 36,
                                           'Vape Distillery': 37,
                                           'VDLV': 38,
                                           'Amazone': 39,
                                           'Aromazon': 40,
                                           'Doctor DIY': 41,
                                           'Fighter Fuel': 42,
                                           'Kyandi Shop': 43,
                                           'Shootiz': 44,
                                           'Vape 47': 45
})
# passe marque_id en numeric (toutes les chaînes de caractères sont remplacées par NaN)
df['marque_id'] = pd.to_numeric(df['marque_id'], errors='coerce').astype('Int64')
# remplace les NaN de marque_id par une valeur numérique NULL pour pouvoir l'insérer dans une base de données mysql
df['marque_id'] = df['marque_id'].replace({pd.NA: None})

# df['marque_id'] = df['marque_id'].replace('[^\d]+', None, regex=True) / inplace=True
# df['marque_id'] = df['marque_id'].replace('', None)
# df['marque_id'] = df['marque_id'].fillna(None)

df['type_saveur_id'] = df['type_saveur_id'].replace({'Classic': 1,
                                                     'Mentholé': 2,
                                                     'Fruité': 3,
                                                     'Fruité Frais': 4,
                                                     'Gourmand': 5,
                                                     'Friandise / Boisson': 6
})
# passe type_saveur_id en numeric (toutes les chaînes de caractères sont remplacées par NaN)
df['type_saveur_id'] = pd.to_numeric(df['type_saveur_id'], errors='coerce').astype('Int64')
# remplace les NaN de type_saveur_id par une valeur numérique NULL pour pouvoir l'insérer dans une base de données mysql
df['type_saveur_id'] = df['type_saveur_id'].replace({pd.NA: None})

# remplace les NaN de description par une valeur numérique NULL pour pouvoir l'insérer dans une base de données mysql
df['description'] = df['description'].replace({pd.NA: None})

df['dosage_pg_vg_id'] = df['dosage_pg_vg_id'].replace({'10/90': 1,
                                                       '20/80': 2,
                                                       '30/70': 3,
                                                       '40/60': 4,
                                                       '50/50': 5,
                                                       '60/40': 6,
                                                       '70/30': 7,
                                                       '76/24': 8
})
# passe dosage_pg_vg_id en numeric (toutes les chaînes de caractères sont remplacées par NaN)
df['dosage_pg_vg_id'] = pd.to_numeric(df['dosage_pg_vg_id'], errors='coerce').astype('Int64')
# remplace les NaN de dosage_pg_vg_id par une valeur numérique NULL pour pouvoir l'insérer dans une base de données mysql
df['dosage_pg_vg_id'] = df['dosage_pg_vg_id'].replace({pd.NA: None})
df['dosage_pg_vg_id'] = df['dosage_pg_vg_id'].replace({'': None})

# passe contenance_ml_id en numeric (toutes les chaînes de caractères sont remplacées par NaN)
df['contenance_ml_id'] = pd.to_numeric(df['contenance_ml_id'], errors='coerce').astype('Int64')
# remplace les NaN de contenance_ml_id par une valeur numérique NULL pour pouvoir l'insérer dans une base de données mysql
df['contenance_ml_id'] = df['contenance_ml_id'].replace({pd.NA: None})
df['contenance_ml_id'] = df['contenance_ml_id'].replace({'': None})
# remplace les valeurs dans la colonne 'contenance_ml_id' en fonction de 'categorie_id' pour 10mL
df['contenance_ml_id'] = np.where((df['categorie_id'] == 1) & (df['contenance_ml_id'] == 10), 1,
                                    np.where((df['categorie_id'] == 1) & (df['contenance_ml_id'] != 10), None, df['contenance_ml_id']))
# remplace les valeurs dans la colonne 'contenance_ml_id' en fonction de 'categorie_id' pour les grands formats
df['contenance_ml_id'] = np.where((df['categorie_id'] == 2) & (df['contenance_ml_id'] > 10) & (df['contenance_ml_id'] < 80), 3,
                                    np.where((df['categorie_id'] == 2) & (df['contenance_ml_id'] >= 80) & (df['contenance_ml_id'] < 100), 4,
                                                np.where((df['categorie_id'] == 2) & (df['contenance_ml_id'] >= 100) & (df['contenance_ml_id'] < 200), 5,
                                                            np.where((df['categorie_id'] == 2) & (df['contenance_ml_id'] >= 200), 6, df['contenance_ml_id']))))
# remplace les valeurs dans la colonne 'contenance_ml_id' en fonction de 'categorie_id' pour concentrés 10 et 30mL
df['contenance_ml_id'] = np.where((df['categorie_id'] == 3) & (df['contenance_ml_id'] == 10), 1,
                                  np.where((df['categorie_id'] == 3) & (df['contenance_ml_id'] == 30), 2,
                                           np.where((df['categorie_id'] == 3) & ((df['contenance_ml_id'] != 10) & (df['contenance_ml_id'] != 30)), None, df['contenance_ml_id'])))
# si la valeur de 'contenance_ml_id' est supérieure à 6, remplace par None
df['contenance_ml_id'] = np.where(df['contenance_ml_id'] > 6, None, df['contenance_ml_id'])
# si la valeur de 'contenance_ml_id' est supérieure à 6, supprimer la ligne
# df = df.drop(df[df['contenance_ml_id'] > 6].index)

# passe dosage_nicotine_mg_id en numeric (toutes les chaînes de caractères sont remplacées par NaN)
df['dosage_nicotine_mg_id'] = pd.to_numeric(df['dosage_nicotine_mg_id'], errors='coerce').astype('Int64')
# remplace les NaN de dosage_nicotine_mg_id par une valeur numérique NULL pour pouvoir l'insérer dans une base de données mysql
df['dosage_nicotine_mg_id'] = df['dosage_nicotine_mg_id'].replace({pd.NA: None})
df['dosage_nicotine_mg_id'] = df['dosage_nicotine_mg_id'].replace({'': None})
# remplace les valeurs dans la colonne 'dosage_nicotine_mg_id' en fonction de 'sel_de_nicotine' True
df['dosage_nicotine_mg_id'] = np.where((df['sel_de_nicotine'] == True) & (df['dosage_nicotine_mg_id'] == 9), 4,
                                    np.where((df['sel_de_nicotine'] == True) & (df['dosage_nicotine_mg_id'] == 10), 4,
                                                np.where((df['sel_de_nicotine'] == True) & (df['dosage_nicotine_mg_id'] == 18), 7,
                                                            np.where((df['sel_de_nicotine'] == True) & (df['dosage_nicotine_mg_id'] == 19), 7,
                                                                        np.where((df['sel_de_nicotine'] == True) & (df['dosage_nicotine_mg_id'] == 20), 7, df['dosage_nicotine_mg_id'])))))
# remplace les valeurs dans la colonne 'dosage_nicotine_mg_id' en fonction de 'sel_de_nicotine' False
df['dosage_nicotine_mg_id'] = np.where((df['sel_de_nicotine'] == False) & (df['dosage_nicotine_mg_id'] == 0), 1,
                                    np.where((df['sel_de_nicotine'] == False) & (df['dosage_nicotine_mg_id'] > 0) & (df['dosage_nicotine_mg_id'] < 6), 2,
                                                np.where((df['sel_de_nicotine'] == False) & (df['dosage_nicotine_mg_id'] >= 6) & (df['dosage_nicotine_mg_id'] < 12), 3,
                                                            np.where((df['sel_de_nicotine'] == False) & (df['dosage_nicotine_mg_id'] >= 12) & (df['dosage_nicotine_mg_id'] < 18), 5,
                                                                        np.where((df['sel_de_nicotine'] == False) & (df['dosage_nicotine_mg_id'] >= 18), 6, df['dosage_nicotine_mg_id'])))))
# si la valeur de 'dosage_nicotine_mg_id' est supérieure à 7, remplace par None
df['dosage_nicotine_mg_id'] = np.where(df['dosage_nicotine_mg_id'] > 7, None, df['dosage_nicotine_mg_id'])
# si la valeur de 'dosage_nicotine_mg_id' est supérieure à 7, supprimer la ligne
# df = df.drop(df[df['dosage_nicotine_mg_id'] > 7].index)

# si categorie_id est un concentré, remplacer le dosage_pg_vg_id par 9
df['dosage_pg_vg_id'] = np.where(df['categorie_id'] == 3, 9, df['dosage_pg_vg_id'])
# si categorie_id est un concentré, rempalcer le dosage_nicotine_mg_id par 1
df['dosage_nicotine_mg_id'] = np.where(df['categorie_id'] == 3, 1, df['dosage_nicotine_mg_id'])

df['statut_produit_id'] = df['statut_produit_id'].replace({'actif': 1, 'inactif': 2})
# passe statut_produit_id en numeric (toutes les chaînes de caractères sont remplacées par NaN)
df['statut_produit_id'] = pd.to_numeric(df['statut_produit_id'], errors='coerce').astype('Int64')
# remplace les NaN de dosage_pg_vg_id par une valeur numérique 2
df['statut_produit_id'] = df['statut_produit_id'].replace({pd.NA: 2})
df['statut_produit_id'] = df['statut_produit_id'].replace({'': 2})

df['statut_reappro_id'] = df['statut_reappro_id'].replace({'actif': 1, 'inactif': 2})
# passe statut_reappro_id en numeric (toutes les chaînes de caractères sont remplacées par NaN)
df['statut_reappro_id'] = pd.to_numeric(df['statut_reappro_id'], errors='coerce').astype('Int64')
# remplace les NaN de statut_reappro_id par une valeur numérique 2
df['statut_reappro_id'] = df['statut_reappro_id'].replace({pd.NA: 2})
df['statut_reappro_id'] = df['statut_reappro_id'].replace({'': 2})

# créer une colonne au début id remplie de None
df.insert(0, 'id', None)



# si la combinaison sku et magasin_id existe déjà dans la base de données alors update uniquement qte_stock, statut_produit_id et statut_reappro_id
# sinon si sku n'existe pas dans la base de données alors insert

# connexion à la base de données MySQL
connection = pymysql.connect(host='localhost',
                             user='theo',
                             password='3630',
                             db='testTeal')

# créer un curseur pour exécuter des requêtes
cursor = connection.cursor()

# boucle sur chaque ligne du DataFrame et exécute l'insertion ou la mise à jour
for _, row in df.iterrows():
    values = (row['id'], row['magasin_id'], row['sku'], row['libelle_produit'], row['libelle_fiche'], row['categorie_id'], row['marque_id'], row['type_saveur_id'], row['description'], row['dosage_pg_vg_id'], row['contenance_ml_id'], row['dosage_nicotine_mg_id'], row['sel_de_nicotine'], row['qte_stock'], row['statut_produit_id'], row['statut_reappro_id'])

    # Vérifier si la combinaison sku et magasin_id existe déjà dans la base de données
    query_select = "SELECT COUNT(*) FROM produits WHERE sku = %s AND (magasin_id = %s OR (magasin_id IS NULL AND %s IS NULL));"
    cursor.execute(query_select, (row['sku'], row['magasin_id'], row['magasin_id']))
    result = cursor.fetchone()
    count = result[0]

    if count > 0:
        # La combinaison existe, effectuer une mise à jour
        query_update = "UPDATE produits SET qte_stock = %s, statut_produit_id = %s, statut_reappro_id = %s WHERE sku = %s AND magasin_id = %s;"
        cursor.execute(query_update, (row['qte_stock'], row['statut_produit_id'], row['statut_reappro_id'], row['sku'], row['magasin_id']))
    else:
        # La combinaison n'existe pas, effectuer une insertion
        query_insert = "INSERT INTO produits (id, magasin_id, sku, libelle_produit, libelle_fiche, categorie_id, marque_id, type_saveur_id, description, dosage_pg_vg_id, contenance_ml_id, dosage_nicotine_mg_id, sel_de_nicotine, qte_stock, statut_produit_id, statut_reappro_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query_insert, values)

# valider les modifications dans la base de données
connection.commit()

# fermer la connexion et le curseur
cursor.close()
connection.close()



# save
df.to_csv('./bdd/metabaseFileAfterScript.csv', sep=';', index=False)