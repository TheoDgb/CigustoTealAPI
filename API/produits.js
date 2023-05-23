const connection = require('./bdd/db.js');

function getProductsPaginatedAndelnans(limit, offset, callback) {
    connection.query(`SELECT magasin_id, libelle_fiche, MIN(description) AS description, MIN(marque_id) AS marque_id, MIN(type_saveur_id) AS type_saveur_id, MIN(contenance_ml_id) AS contenance_ml_id, MIN(dosage_nicotine_mg_id) AS dosage_nicotine_mg_id, MIN(sel_de_nicotine) AS sel_de_nicotine
                      FROM produits
                      WHERE magasin_id = 1 AND categorie_id != 3
                      GROUP BY magasin_id, libelle_fiche;`, (error, results) => {
    if (error) {
            return callback(error, null);
        }
        return callback(null, results);
    });
}
function getProductsPaginatedBessoncourt(limit, offset, callback) {
    connection.query(`SELECT * FROM produits WHERE magasin_id = 2 AND categorie_id != 3 LIMIT ${limit} OFFSET ${offset}`, (error, results) => {
        if (error) {
            return callback(error, null);
        }
        return callback(null, results);
    });
}
function getProductsPaginatedBesancon(limit, offset, callback) {
    connection.query(`SELECT * FROM produits WHERE magasin_id = 3 AND categorie_id != 3 LIMIT ${limit} OFFSET ${offset}`, (error, results) => {
        if (error) {
            return callback(error, null);
        }
        return callback(null, results);
    });
}
function getProductsPaginatedColmar(limit, offset, callback) {
    connection.query(`SELECT * FROM produits WHERE magasin_id = 4 AND categorie_id != 3 LIMIT ${limit} OFFSET ${offset}`, (error, results) => {
        if (error) {
            return callback(error, null);
        }
        return callback(null, results);
    });
}

module.exports = {
    getProductsPaginatedAndelnans,
    getProductsPaginatedBessoncourt,
    getProductsPaginatedBesancon,
    getProductsPaginatedColmar
};