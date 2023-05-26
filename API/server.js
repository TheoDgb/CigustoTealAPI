const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const {PythonShell} = require('python-shell');
const produits = require('./produits');

const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json({limit: '50mb'}));
app.use(bodyParser.urlencoded({limit: '50mb', extended: true}));
app.use(express.static('public'));

app.get('/magasin-andelnans/e-liquides/all/:magasinId', (req, res) => {
    const magasinId = req.params.magasinId;
    const limit = 10000; // en attendant pour peut etre chargement infini
    const offset = 0;

    switch (magasinId) {
        case '1':
            produits.getELiquidesProduitsAndelnans(limit, offset, (error, results) => {
                if (error) {
                    res.status(500).json({ error: 'Une erreur s\'est produite lors de la récupération des produits' });
                } else {
                    // console.log(results);
                    res.json(results);
                }
            });
            break;
        case '2':
            produits.getELiquidesProduitsBessoncourt(limit, offset, (error, results) => {
                if (error) {
                    res.status(500).json({ error: 'Une erreur s\'est produite lors de la récupération des produits' });
                } else {
                    res.json(results);
                }
            });
            break;
        case '3':
            produits.getELiquidesProduitsBesancon(limit, offset, (error, results) => {
                if (error) {
                    res.status(500).json({ error: 'Une erreur s\'est produite lors de la récupération des produits' });
                } else {
                    res.json(results);
                }
            });
            break;
        case '4':
            produits.getELiquidesProduitsColmar(limit, offset, (error, results) => {
                if (error) {
                    res.status(500).json({ error: 'Une erreur s\'est produite lors de la récupération des produits' });
                } else {
                    res.json(results);
                }
            });
            break;
        default:
            break;
    }
});

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

const options = {
    scriptPath: './bdd'
};
PythonShell.run('script_update_csv.py', options, function (err) {
    if (err) throw err;
    // console.log('Script exécuté avec succès !');
});

PythonShell.run('script_update_image.py', options, function (err) {
    if (err) throw err;
});