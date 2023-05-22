const mysql = require('mysql2');

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'theo',
    password: '3630',
    database: 'testTeal'
});

module.exports = connection;