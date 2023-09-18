import os
import pymysql

# SUPPRIME LE FICHIER saveBDD.csv SI IL EXISTE
chemin_fichier = '/var/lib/mysql-files/saveBDD.csv'
if os.path.exists(chemin_fichier):
    os.remove(chemin_fichier)
    print(f'Le fichier {chemin_fichier} a été supprimé avec succès.')
else:
    print(f'Le fichier {chemin_fichier} n\'existe pas.')


# EXPORTER LA BDD EN CSV
# Chemin du fichier de sortie
output_file = '/var/lib/mysql-files/saveBDD.csv'

connection = pymysql.connect(host='localhost',
                             user='theo',
                             password='3630',
                             db='testTeal')

try:
    # Créez un curseur pour exécuter la requête SQL
    with connection.cursor() as cursor:
        # Votre requête SQL ici
        sql_query = """
        SELECT 'id', 'magasin_id', 'sku', 'libelle_produit', 'libelle_fiche', 'categorie_id', 'marque_id', 'type_saveur_id', 'description', 'dosage_pg_vg_id', 'contenance_ml_id', 'dosage_nicotine_mg_id', 'sel_de_nicotine', 'qte_stock', 'statut_produit_id', 'statut_reappro_id'
        UNION
        SELECT id, magasin_id, sku, libelle_produit, libelle_fiche, categorie_id, marque_id, type_saveur_id, description, dosage_pg_vg_id, contenance_ml_id, dosage_nicotine_mg_id, sel_de_nicotine, qte_stock, statut_produit_id, statut_reappro_id
        INTO OUTFILE %s
        FIELDS TERMINATED BY ';' OPTIONALLY ENCLOSED BY '"' ESCAPED BY ''
        LINES TERMINATED BY '\n'
        FROM testTeal.produits;
        """
        cursor.execute(sql_query, (output_file,))

    # Validez la transaction
    connection.commit()

    print(f'Le fichier {output_file} a été généré avec succès.')

finally:
    # Fermez la connexion MySQL
    connection.close()

# RESET LA BDD
connection = pymysql.connect(host='localhost',
                             user='theo',
                             password='3630',
                             db='testTeal')

# Créer un curseur pour exécuter les commandes SQL
cursor = connection.cursor()

# Les commandes SQL que vous souhaitez exécuter
sql_commands = [
    "USE testTeal;",
    "DROP TABLE IF EXISTS produits;",
    "DROP TABLE IF EXISTS statut_reappros;",
    "DROP TABLE IF EXISTS statut_produits;",
    "DROP TABLE IF EXISTS dosages_nicotine_mg;",
    "DROP TABLE IF EXISTS contenances_ml;",
    "DROP TABLE IF EXISTS dosages_pg_vg;",
    "DROP TABLE IF EXISTS type_saveurs;",
    "DROP TABLE IF EXISTS marques;",
    "DROP TABLE IF EXISTS categories;",
    "DROP TABLE IF EXISTS magasins;",

    "CREATE TABLE magasins (id INT PRIMARY KEY NOT NULL, libelle_magasin VARCHAR(75) NOT NULL);",
    "CREATE TABLE categories (id INT PRIMARY KEY NOT NULL, libelle_categorie VARCHAR(21) NOT NULL);",
    "CREATE TABLE marques (id INT PRIMARY KEY NOT NULL, libelle_marque VARCHAR(50) NOT NULL);",
    "CREATE TABLE type_saveurs (id INT PRIMARY KEY NOT NULL, libelle_type_saveur VARCHAR(30) NOT NULL);",
    "CREATE TABLE dosages_pg_vg (id INT PRIMARY KEY NOT NULL, libelle_dosage_pg_vg VARCHAR(5) NOT NULL);",
    "CREATE TABLE contenances_ml (id INT PRIMARY KEY NOT NULL, contenance_ml INT NOT NULL);",
    "CREATE TABLE dosages_nicotine_mg (id INT PRIMARY KEY NOT NULL, dosage_nicotine_mg INT NOT NULL);",
    "CREATE TABLE statut_produits (id INT PRIMARY KEY NOT NULL, libelle_statut_produit VARCHAR(23) NOT NULL);",

    "CREATE TABLE statut_reappros (id INT PRIMARY KEY NOT NULL, libelle_statut_reappro VARCHAR(23) NOT NULL);",

    "CREATE TABLE produits (id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, magasin_id INT, sku VARCHAR(8) NOT NULL, FOREIGN KEY (magasin_id) REFERENCES magasins(id), libelle_produit VARCHAR(100) NOT NULL, libelle_fiche VARCHAR(100) NOT NULL, categorie_id INT NOT NULL, FOREIGN KEY (categorie_id) REFERENCES categories(id), marque_id INT, FOREIGN KEY (marque_id) REFERENCES marques(id), type_saveur_id INT, FOREIGN KEY (type_saveur_id) REFERENCES type_saveurs(id), description VARCHAR(100), dosage_pg_vg_id INT, FOREIGN KEY (dosage_pg_vg_id) REFERENCES dosages_pg_vg(id), contenance_ml_id INT, FOREIGN KEY (contenance_ml_id) REFERENCES contenances_ml(id), dosage_nicotine_mg_id INT, FOREIGN KEY (dosage_nicotine_mg_id) REFERENCES dosages_nicotine_mg(id), sel_de_nicotine BOOLEAN NOT NULL, qte_stock INT NOT NULL, statut_produit_id INT, FOREIGN KEY (statut_produit_id) REFERENCES statut_produits(id), statut_reappro_id INT, FOREIGN KEY (statut_reappro_id) REFERENCES statut_reappros(id));",

    "INSERT INTO magasins (id, libelle_magasin) VALUES (1, 'CIGUSTO ANDELNANS'), (2, 'CIGUSTO BESANCON ECOLE VALENTIN'), (3, 'CIGUSTO BESSONCOURT'), (4, 'CIGUSTO COLMAR - HOUSSEN');",

    "INSERT INTO categories (id, libelle_categorie) VALUES (1, 'Liquides 10 ml'), (2, 'Liquides Grand Format'), (3, 'Concentrés');",

    "INSERT INTO marques (id, libelle_marque) VALUES (1, 'A&L'), (2, 'Alfaliquid'), (3, 'Bakery Shake'), (4, 'Candy Shake'), (5, 'Cesar'), (6, 'Cigusto'), (7, 'CirKus'), (8, 'Curieux'), (9, 'Don Cristo'), (10, 'Eliquid France'), (11, 'Enfer'), (12, 'E.Tasty'), (13, 'Fresh Vape Co'), (14, 'Fruiteo'), (15, 'Fruity Cool'), (16, 'Fruity Fuel'), (17, 'Fruizee'), (18, 'Full Moon'), (19, 'Furiosa'), (20, 'Greeneo'), (21, 'Juicy Shake'), (22, 'Kung Fruits'), (23, 'Le Coq Qui Vape'), (24, 'Le French Liquide'), (25, 'Le Vapoteur Breton'), (26, 'Les Devils'), (27, 'Liquideo'), (28, 'Mono'), (29, 'Monster'), (30, 'Petit Nuage'), (31, 'Salt E-vapor'), (32, 'Snap Dragon'), (33, 'Swoke'), (34, 'The Medusa Juice'), (35, 'T-Juice'), (36, 'Vampire Vape'), (37, 'Vape Distillery'), (38, 'VDLV'), (39, 'Amazone'), (40, 'Aromazon'), (41, 'Doctor Diy'), (42, 'Fighter Fuel'), (43, 'Kyandi Shop'), (44, 'Shootiz'), (45, 'Vape47');",

    "INSERT INTO type_saveurs (id, libelle_type_saveur) VALUES (1, 'Classic'), (2, 'Mentholé'), (3, 'Fruité'), (4, 'Fruité Frais'), (5, 'Gourmand'), (6, 'Friandise / Boisson');",

    "INSERT INTO dosages_pg_vg (id, libelle_dosage_pg_vg) VALUES (1, '10/90'), (2, '20/80'), (3, '30/70'), (4, '40/60'), (5, '50/50'), (6, '60/40'), (7, '70/30'), (8, '76/24'), (9, 'false');",

    "INSERT INTO contenances_ml (id, contenance_ml) VALUES (1, 10), (2, 30), (3, 50), (4, 80), (5, 100), (6, 200);",

    "INSERT INTO dosages_nicotine_mg (id, dosage_nicotine_mg) VALUES (1, 0), (2, 3), (3, 6), (4, 910), (5, 12), (6, 18), (7, 1820);",

    "INSERT INTO statut_produits (id, libelle_statut_produit) VALUES (1, 'actif'), (2, 'inactif');",

    "INSERT INTO statut_reappros (id, libelle_statut_reappro) VALUES (1, 'actif'), (2, 'inactif');"
]

# Exécutez chaque commande SQL
for sql_command in sql_commands:
    cursor.execute(sql_command)

# Validez les changements dans la base de données
connection.commit()

# Fermez le curseur et la connexion
cursor.close()
connection.close()