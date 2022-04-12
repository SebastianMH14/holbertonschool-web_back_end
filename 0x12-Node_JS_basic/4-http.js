const app = require('http');

const port = 1245;

const helloWorld = ((req, res) => {
  res.writeHead(200);
  res.end('Hello Holberton School!');
});

const server = app.createServer(helloWorld);
server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});

module.exports = app;