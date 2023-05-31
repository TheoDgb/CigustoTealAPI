const connection = require('./bdd/db.js');

function getELiquidesProduitsAndelnans(limit, offset, callback) {
    // connection.query(`SELECT magasin_id, libelle_fiche, MIN(description) AS description, MIN(marque_id) AS marque_id, MIN(type_saveur_id) AS type_saveur_id, MIN(contenance_ml_id) AS contenance_ml_id, MIN(dosage_nicotine_mg_id) AS dosage_nicotine_mg_id, MIN(sel_de_nicotine) AS sel_de_nicotine
    //                   FROM produits
    //                   WHERE magasin_id = 1 AND categorie_id != 3
    //                   GROUP BY magasin_id, libelle_fiche;`, (error, results) => {
    connection.query(`SELECT
                          magasin_id,
                          libelle_fiche,
                          MIN(libelle_produit) AS libelle_produit,
                          MIN(sku) AS sku,
                          MIN(description) AS description,
                          MIN(marque_id) AS marque_id,
                          MIN(type_saveur_id) AS type_saveur_id,
                          MIN(dosage_pg_vg_id) AS dosage_pg_vg_id,
                          MIN(contenance_ml_id) AS contenance_ml_id,
                          GROUP_CONCAT(DISTINCT dosage_nicotine_mg_id) AS dosage_nicotine_mg_id,
                          MIN(sel_de_nicotine) AS sel_de_nicotine,
                          MIN(statut_produit_id) AS statut_produit_id
                      FROM produits
                      WHERE magasin_id = 1 AND categorie_id != 3 AND statut_produit_id != 2
                      GROUP BY magasin_id, libelle_fiche;`, (error, results) => {
    if (error) {
            return callback(error, null);
        }
        return callback(null, results);
    });
}
function getELiquidesProduitsBessoncourt(limit, offset, callback) {
    connection.query(`SELECT
                          magasin_id,
                          MIN(sku) AS sku,
                          libelle_fiche,
                          MIN(sku) AS sku,
                          MIN(description) AS description,
                          MIN(marque_id) AS marque_id,
                          MIN(type_saveur_id) AS type_saveur_id,
                          MIN(dosage_pg_vg_id) AS dosage_pg_vg_id,
                          MIN(contenance_ml_id) AS contenance_ml_id,
                          GROUP_CONCAT(DISTINCT dosage_nicotine_mg_id) AS dosage_nicotine_mg_id,
                          MIN(sel_de_nicotine) AS sel_de_nicotine,
                          MIN(statut_produit_id) AS statut_produit_id
                      FROM produits
                      WHERE magasin_id = 2 AND categorie_id != 3 AND statut_produit_id != 2
                      GROUP BY magasin_id, libelle_fiche;`, (error, results) => {
        if (error) {
            return callback(error, null);
        }
        return callback(null, results);
    });
}
function getELiquidesProduitsBesancon(limit, offset, callback) {
    connection.query(`SELECT
                          magasin_id,
                          MIN(sku) AS sku,
                          libelle_fiche,
                          MIN(sku) AS sku,
                          MIN(description) AS description,
                          MIN(marque_id) AS marque_id,
                          MIN(type_saveur_id) AS type_saveur_id,
                          MIN(dosage_pg_vg_id) AS dosage_pg_vg_id,
                          MIN(contenance_ml_id) AS contenance_ml_id,
                          GROUP_CONCAT(DISTINCT dosage_nicotine_mg_id) AS dosage_nicotine_mg_id,
                          MIN(sel_de_nicotine) AS sel_de_nicotine,
                          MIN(statut_produit_id) AS statut_produit_id
                      FROM produits
                      WHERE magasin_id = 3 AND categorie_id != 3 AND statut_produit_id != 2
                      GROUP BY magasin_id, libelle_fiche;`, (error, results) => {
        if (error) {
            return callback(error, null);
        }
        return callback(null, results);
    });
}
function getELiquidesProduitsColmar(limit, offset, callback) {
    connection.query(`SELECT
                          magasin_id,
                          MIN(sku) AS sku,
                          libelle_fiche,
                          MIN(sku) AS sku,
                          MIN(description) AS description,
                          MIN(marque_id) AS marque_id,
                          MIN(type_saveur_id) AS type_saveur_id,
                          MIN(dosage_pg_vg_id) AS dosage_pg_vg_id,
                          MIN(contenance_ml_id) AS contenance_ml_id,
                          GROUP_CONCAT(DISTINCT dosage_nicotine_mg_id) AS dosage_nicotine_mg_id,
                          MIN(sel_de_nicotine) AS sel_de_nicotine,
                          MIN(statut_produit_id) AS statut_produit_id
                      FROM produits
                      WHERE magasin_id = 4 AND categorie_id != 3 AND statut_produit_id != 2
                      GROUP BY magasin_id, libelle_fiche;`, (error, results) => {
        if (error) {
            return callback(error, null);
        }
        return callback(null, results);
    });
}

function getConcentresProduitsAndelnans(limit, offset, callback) {
    connection.query(`SELECT
                          magasin_id,
                          MIN(sku) AS sku,
                          libelle_fiche,
                          MIN(sku) AS sku,
                          MIN(description) AS description,
                          MIN(marque_id) AS marque_id,
                          MIN(type_saveur_id) AS type_saveur_id,
                          MIN(dosage_pg_vg_id) AS dosage_pg_vg_id,
                          MIN(contenance_ml_id) AS contenance_ml_id,
                          GROUP_CONCAT(DISTINCT dosage_nicotine_mg_id) AS dosage_nicotine_mg_id,
                          MIN(sel_de_nicotine) AS sel_de_nicotine,
                          MIN(statut_produit_id) AS statut_produit_id
                      FROM produits
                      WHERE magasin_id = 1 AND categorie_id = 3 AND statut_produit_id != 2
                      GROUP BY magasin_id, libelle_fiche;`, (error, results) => {
        if (error) {
            return callback(error, null);
        }
        return callback(null, results);
    });
}
function getConcentresProduitsBessoncourt(limit, offset, callback) {
    connection.query(`SELECT
                          magasin_id,
                          MIN(sku) AS sku,
                          libelle_fiche,
                          MIN(sku) AS sku,
                          MIN(description) AS description,
                          MIN(marque_id) AS marque_id,
                          MIN(type_saveur_id) AS type_saveur_id,
                          MIN(dosage_pg_vg_id) AS dosage_pg_vg_id,
                          MIN(contenance_ml_id) AS contenance_ml_id,
                          GROUP_CONCAT(DISTINCT dosage_nicotine_mg_id) AS dosage_nicotine_mg_id,
                          MIN(sel_de_nicotine) AS sel_de_nicotine,
                          MIN(statut_produit_id) AS statut_produit_id
                      FROM produits
                      WHERE magasin_id = 2 AND categorie_id = 3 AND statut_produit_id != 2
                      GROUP BY magasin_id, libelle_fiche;`, (error, results) => {
        if (error) {
            return callback(error, null);
        }
        return callback(null, results);
    });
}
function getConcentresProduitsBesancon(limit, offset, callback) {
    connection.query(`SELECT
                          magasin_id,
                          MIN(sku) AS sku,
                          libelle_fiche,
                          MIN(sku) AS sku,
                          MIN(description) AS description,
                          MIN(marque_id) AS marque_id,
                          MIN(type_saveur_id) AS type_saveur_id,
                          MIN(dosage_pg_vg_id) AS dosage_pg_vg_id,
                          MIN(contenance_ml_id) AS contenance_ml_id,
                          GROUP_CONCAT(DISTINCT dosage_nicotine_mg_id) AS dosage_nicotine_mg_id,
                          MIN(sel_de_nicotine) AS sel_de_nicotine,
                          MIN(statut_produit_id) AS statut_produit_id
                      FROM produits
                      WHERE magasin_id = 3 AND categorie_id = 3 AND statut_produit_id != 2
                      GROUP BY magasin_id, libelle_fiche;`, (error, results) => {
        if (error) {
            return callback(error, null);
        }
        return callback(null, results);
    });
}
function getConcentresProduitsColmar(limit, offset, callback) {
    connection.query(`SELECT
                          magasin_id,
                          MIN(sku) AS sku,
                          libelle_fiche,
                          MIN(sku) AS sku,
                          MIN(description) AS description,
                          MIN(marque_id) AS marque_id,
                          MIN(type_saveur_id) AS type_saveur_id,
                          MIN(dosage_pg_vg_id) AS dosage_pg_vg_id,
                          MIN(contenance_ml_id) AS contenance_ml_id,
                          GROUP_CONCAT(DISTINCT dosage_nicotine_mg_id) AS dosage_nicotine_mg_id,
                          MIN(sel_de_nicotine) AS sel_de_nicotine,
                          MIN(statut_produit_id) AS statut_produit_id
                      FROM produits
                      WHERE magasin_id = 4 AND categorie_id = 3 AND statut_produit_id != 2
                      GROUP BY magasin_id, libelle_fiche;`, (error, results) => {
        if (error) {
            return callback(error, null);
        }
        return callback(null, results);
    });
}

module.exports = {
    getELiquidesProduitsAndelnans,
    getELiquidesProduitsBessoncourt,
    getELiquidesProduitsBesancon,
    getELiquidesProduitsColmar
    // ,
    // getConcentresProduitsAndelnans,
    // getConcentresProduitsBessoncourt,
    // getConcentresProduitsBesancon,
    // getConcentresProduitsColmar
};