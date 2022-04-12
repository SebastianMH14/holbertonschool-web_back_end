const http = require('http');

const port = 1245;

const helloWorld = ((req, res) => {
  res.writeHead(200);
  res.end('Hello Holberton School!');
});

const app = http.createServer(helloWorld);
server.listen(port);

module.exports = app;
