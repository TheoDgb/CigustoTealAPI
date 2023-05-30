const controller = require('../controllers/controller.js');

module.exports = function(app){
    app.get('/magasin-andelnans', controller.magasin_andelnans);
    app.get('/magasin-bessoncourt', controller.magasin_bessoncourt);
    app.get('/magasin-besancon', controller.magasin_besancon);
    app.get('/magasin-colmar', controller.magasin_colmar);

    app.get('/magasin-andelnans/nouveautes', controller.magasin_andelnans_nouveautes);
    app.get('/magasin-bessoncourt/nouveautes', controller.magasin_bessoncourt_nouveautes);
    app.get('/magasin-besancon/nouveautes', controller.magasin_besancon_nouveautes);
    app.get('/magasin-colmar/nouveautes', controller.magasin_colmar_nouveautes);

    app.get('/magasin-andelnans/coups-de-coeur', controller.magasin_andelnans_coups_de_coeur);
    app.get('/magasin-bessoncourt/coups-de-coeur', controller.magasin_bessoncourt_coups_de_coeur);
    app.get('/magasin-besancon/coups-de-coeur', controller.magasin_besancon_coups_de_coeur);
    app.get('/magasin-colmar/coups-de-coeur', controller.magasin_colmar_coups_de_coeur);

    app.get('/magasin-andelnans/e-liquides', controller.magasin_andelnans_e_liquides);
    app.get('/magasin-bessoncourt/e-liquides', controller.magasin_bessoncourt_e_liquides);
    app.get('/magasin-besancon/e-liquides', controller.magasin_besancon_e_liquides);
    app.get('/magasin-colmar/e-liquides', controller.magasin_colmar_e_liquides);

    app.get('/magasin-andelnans/concentres', controller.magasin_andelnans_concentres);
    app.get('/magasin-bessoncourt/concentres', controller.magasin_bessoncourt_concentres);
    app.get('/magasin-besancon/concentres', controller.magasin_besancon_concentres);
    app.get('/magasin-colmar/concentres', controller.magasin_colmar_concentres);
}