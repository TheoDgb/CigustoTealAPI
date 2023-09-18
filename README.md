# CigustoTealAPI

## npm run start

### su - | mysql | use testTeal

### http://localhost:3000/
### http://localhost:3000/magasin-andelnans/e-liquides
### http://localhost:3000/gestion-produits

### test tel : http://192.168.47.252:3000/



# METTRE A JOUR LA BDD UNE FOIS LES MODIFICATIONS REALISEES SUR /gestion-produits

# chemin d'exportation : SHOW VARIABLES LIKE "secure_file_priv"

# 1 : exporter les données de la table produits dans un fichier csv depuis mysql
# SELECT 'id', 'magasin_id', 'sku', 'libelle_produit', 'libelle_fiche', 'categorie_id', 'marque_id', 'type_saveur_id', 'description', 'dosage_pg_vg_id', 'contenance_ml_id', 'dosage_nicotine_mg_id', 'sel_de_nicotine', 'qte_stock', 'statut_produit_id', 'statut_reappro_id'
# UNION
# SELECT id, magasin_id, sku, libelle_produit, libelle_fiche, categorie_id, marque_id, type_saveur_id, description, dosage_pg_vg_id, contenance_ml_id, dosage_nicotine_mg_id, sel_de_nicotine, qte_stock, statut_produit_id, statut_reappro_id
# INTO OUTFILE '/var/lib/mysql-files/saveBDD.csv'
# FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '"' ESCAPED BY ''
# LINES TERMINATED BY '\n'
# FROM testTeal.produits;

# 2 : RESET LES TABLES (exécuter db.sql)

# 1-2 ||
# aller dans cd Documents/GitHub/CigustoTealAPI/API/bdd
# sudo python3 exportbdd.py

# 3 : supprimer saveBDD et saveBDDAfterScript
# déplacer le fichier /var/lib/mysql-files/saveBDD.csv dans ./bdd

# 4 : aller dans cd Documents/GitHub/CigustoTealAPI/API/bdd
# réimporter les données : python3 script_reintegration_csv_save.py

# redémarrer le serveur retéléchargera un fichier MetaBase à jour et intégrera les données dans la BDD via script_update_csv.py :
# si le produit (sku + magasin_id) existe déjà, uniquement qte_stock, statut_produit_id et statut_reappro_id seront mis à jour
# sinon le produit sera créé

# Étant donné le nombre faramineux d'erreurs, dans la BDD MetaBase fournie, qu'il y a à corriger, il est conseillé d'exporter le plus souvent possible les données de la BDD afin d'éviter des pertes de données.