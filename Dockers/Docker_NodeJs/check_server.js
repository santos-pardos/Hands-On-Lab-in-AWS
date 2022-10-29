var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Welcome to Node.js Server');
}).listen(3000, "0.0.0.0");
console.log('Server running at http://myippublica:3000/');