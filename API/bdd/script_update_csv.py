import pandas as pd
import numpy as np

df = pd.read_csv('./bdd/test.csv', sep=';', decimal=',')

# supprime les colonnes inutiles
df = df.drop(['ID','Sku', 'EAN', 'PV ttc Preco', 'Marge Ht préco', 'tx marge preco', 'PA ht centrale', 'PV TTC magasin', 'Marge ht magasin', 'tx de marge magasin'], axis=1)

# remplace NaN par 0
df['Qté stock'] = df['Qté stock'].fillna(0)
# convertit la colonne Qté stock en entier
df['Qté stock'] = df['Qté stock'].astype(int)

# renommer les colonnes pour les rendre utilisables dans la bdd
df = df.rename(columns={
    'libellé fiche': 'libelle_fiche',
    'libellé produit': 'libelle_produit',
    'catégorie': 'categorie_id',
    'gamme': 'gamme',
    'Marque': 'marque_id',
    'description': 'description',
    'type saveur': 'type_saveur_id',
    'dosage Pg/Vg': 'dosage_pg_vg_id',
    'dosage nicotine': 'dosage_nicotine_mg_id',
    'volume flacon': 'contenance_ml_id',
    'sel de nicotine': 'sel_de_nicotine',
    'Magasin': 'magasin_id',
    'Qté stock': 'qte_stock'
})

# supprime les lignes qui ne sont pas des liquides / concentrés
df = df[df['categorie_id'].isin(["Liquides 10 ml", "Liquides Grand Format", "Concentrés"])]

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
df = df.reindex(columns=['magasin_id', 'libelle_produit', 'libelle_fiche', 'categorie_id', 'marque_id', 'type_saveur_id', 'description', 'dosage_pg_vg_id', 'contenance_ml_id', 'dosage_nicotine_mg_id', 'sel_de_nicotine', 'qte_stock'])

# save
df.to_csv('./bdd/test.csv', sep=';', index=False)