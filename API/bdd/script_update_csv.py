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
    'catégorie': 'categorie',
    'gamme': 'gamme',
    'Marque': 'marque',
    'description': 'description',
    'type saveur': 'type_saveur',
    'dosage Pg/Vg': 'dosage_pg_vg',
    'dosage nicotine': 'dosage_nicotine_mg',
    'volume flacon': 'volume_flacon_ml',
    'sel de nicotine': 'sel_de_nicotine',
    'Magasin': 'magasin',
    'Qté stock': 'qte_stock'
})

# supprime les lignes qui ne sont pas des liquides / concentrés
df = df[df['categorie'].isin(["Liquides 10 ml", "Liquides Grand Format", "Concentrés"])]

# supprimer "mg"
df['dosage_nicotine_mg'] = df['dosage_nicotine_mg'].str.replace('mg', '')
 # convertir dosage_nicotine_mg en entiers
df['dosage_nicotine_mg'] = pd.to_numeric(df['dosage_nicotine_mg'], errors='coerce').astype('Int64')

# supprimer "ml"
df['volume_flacon_ml'] = df['volume_flacon_ml'].str.replace('ml', '')
 # convertir volume_flacon_ml en entiers
df['volume_flacon_ml'] = pd.to_numeric(df['volume_flacon_ml'], errors='coerce').astype('Int64')

# remplace "oui" par True et vide par False
df['sel_de_nicotine'] = df['sel_de_nicotine'].replace({'oui': True}).fillna(False)

# déplacement de certains champs de gamme vers marque
mask = df["gamme"] == "Cesar"
df.loc[mask, "marque"] = "Cesar"
mask = df["gamme"] == "Devil's"
df.loc[mask, "marque"] = "Devil's"
mask = df["gamme"] == "Devil sels de nicotine en Devil's" #erreur de saisie ? o.O
df.loc[mask, "marque"] = "Devil's"
mask = df["gamme"] == "Salt-E-vapor"
df.loc[mask, "marque"] = "Salt-E-vapor"
mask = df["gamme"] == "Fruizee"
df.loc[mask, "marque"] = "Fruizee"
mask = df["gamme"] == "Kung Fruits"
df.loc[mask, "marque"] = "Kung Fruits"
mask = df["gamme"] == "Le Coq qui vape"
df.loc[mask, "marque"] = "Le Coq qui vape"
mask = df["gamme"] == "Mono+"
df.loc[mask, "marque"] = "Mono+"
mask = df["gamme"] == "Enfer"
df.loc[mask, "marque"] = "Enfer"

# suppression de la colonne gamme
df.drop('gamme', axis=1)

# réorganise les colonnes
df = df.reindex(columns=['magasin', 'libelle_produit', 'libelle_fiche', 'categorie', 'marque', 'type_saveur', 'description', 'dosage_pg_vg', 'dosage_nicotine_mg', 'volume_flacon_ml', 'sel_de_nicotine', 'qte_stock'])

# save
df.to_csv('./bdd/test.csv', sep=';', index=False)