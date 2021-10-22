/*jshint node:true*/

let express = require("express");
let bodyParser = require('body-parser');
let apiv1 = require('./routes/apiv1.js');
let EJS = require('ejs');

EJS.open = "<ejs>";
EJS.close = "</ejs>";

let host = process.env.PORT ? '0.0.0.0' : 'localhost';
let port = (process.env.PORT || 5000);
let url = require('url').format({hostname: host, port: port, protocol: 'http'});

let app = express();
app.use(express.static('static'));
app.set('view engine', 'ejs');

app.use( bodyParser.json() ); 
app.use(bodyParser.urlencoded({
  extended: false
}));
app.use('/api/v1/', apiv1.router);

let http = require('http');
let server = http.createServer(app);
server.listen(port, function () {
    console.log('Weather Report listening on ' + url);
});

app.get("/", function(req, res) {
    return res.render('main');
});
