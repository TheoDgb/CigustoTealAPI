const connection = require('./bdd/db.js');

function getProductsPaginatedAndelnans(limit, offset, callback) {
    connection.query(`SELECT * FROM produits WHERE magasin_id = 1 AND categorie_id != 3 LIMIT ${limit} OFFSET ${offset}`, (error, results) => {
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