USE testTeal;

# CREATE TABLE caracteristiques (
#     id INT PRIMARY KEY NOT NULL,
#     libelle_fiche VARCHAR(100) NOT NULL,
#     categorie VARCHAR(50),
#     gamme VARCHAR(50),
#     marque VARCHAR(50),
#     description VARCHAR(150),
#     type_saveur VARCHAR(50),
#     volume_flacon INT,
#     sel_de_nicotine BOOLEAN
# );
#
# CREATE TABLE magasins (
#     id INT PRIMARY KEY NOT NULL,
#     nom VARCHAR(100) NOT NULL
# );
#
# CREATE TABLE produits (
#   id INT AUTO_INCREMENT PRIMARY KEY,
#   libelle_produit VARCHAR(100) NOT NULL,
#   dosage_nicotine INT,
#   dosage_pg_vg VARCHAR(10),
#   magasin_id INT NOT NULL,
#         FOREIGN KEY (magasin_id) REFERENCES magasins(id),
#   caracteristique_id INT NOT NULL,
#         FOREIGN KEY (caracteristique_id) REFERENCES caracteristiques(id)
# );


CREATE TABLE magasins (
    id INT PRIMARY KEY NOT NULL,
    nom_magasin VARCHAR(75) NOT NULL
);

CREATE TABLE produits (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    magasin_id INT NOT NULL,
        FOREIGN KEY (magasin_id) REFERENCES magasins(id),
    libelle_produit VARCHAR(100) NOT NULL,
    libelle_fiche VARCHAR(100) NOT NULL
);



# test
INSERT INTO magasins (id, nom_magasin)
VALUES (1, 'CIGUSTO ANDELNANS'),
       (2, 'CIGUSTO BESANCON ECOLE VALENTIN'),
       (3, 'CIGUSTO BESSONCOURT'),
       (4, 'CIGUSTO COLMAR - HOUSSEN');

INSERT INTO produits (id, magasin_id, libelle_produit, libelle_fiche)
VALUES (null, 1, 'E Liquide RED ASTAIRE - T-Juice - 10 ml 0 mg', 'E Liquide RED ASTAIRE 10 ml - Tjuice');