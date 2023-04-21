const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));
app.use(express.static('public'));

// selection magasin
app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`)
});

// home magasin
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'magasin.html'))
});
app.get('/magasin-andelnans', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'home.html'))
});
app.get('/magasin-bessoncourt', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'home.html'))
});
app.get('/magasin-besancon', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'home.html'))
});
app.get('/magasin-colmar', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'home.html'))
});

// nouveautés magasin
app.get('/magasin-andelnans/nouveautes', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'nouveautes.html'))
});
app.get('/magasin-bessoncourt/nouveautes', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'nouveautes.html'))
});
app.get('/magasin-besancon/nouveautes', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'nouveautes.html'))
});
app.get('/magasin-colmar/nouveautes', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'nouveautes.html'))
});

// coups de coeur magasin
app.get('/magasin-andelnans/coups-de-coeur', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'coups-de-coeur.html'))
});
app.get('/magasin-bessoncourt/coups-de-coeur', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'coups-de-coeur.html'))
});
app.get('/magasin-besancon/coups-de-coeur', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'coups-de-coeur.html'))
});
app.get('/magasin-colmar/coups-de-coeur', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'coups-de-coeur.html'))
});

// e-liquides magasin
app.get('/magasin-andelnans/e-liquides', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'e-liquides.html'))
});
app.get('/magasin-bessoncourt/e-liquides', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'e-liquides.html'))
});
app.get('/magasin-besancon/e-liquides', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'e-liquides.html'))
});
app.get('/magasin-colmar/e-liquides', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'e-liquides.html'))
});

// concentrés magasin
app.get('/magasin-andelnans/concentres', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'concentres.html'))
});
app.get('/magasin-bessoncourt/concentres', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'concentres.html'))
});
app.get('/magasin-besancon/concentres', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'concentres.html'))
});
app.get('/magasin-colmar/concentres', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'concentres.html'))
});