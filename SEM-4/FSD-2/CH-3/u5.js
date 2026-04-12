var https = require('http')
var fs = require('fs');
https.createServer(function (req, res) {

    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(`
            <html>
                <body>
                    <h1 style="color:blue;">Welcome</h1>
                </body>
            </html>
        `)
        res.end();
    }
    else if (req.url == '/login') {
        fs.readFile('q.html', (err,data) => {
            if (err) {
                res.writeHead(404)
                res.end()
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(data)
            }
        });
    }
    else if (req.url === '/gallery') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(`
            <html>
                <body>
                    <h1>This is image page</h1>
                </body>
            </html>
        `)
        res.end();
    }
    else {
        res.writeHead(404, { 'content-type': 'text/html' })
        res.write('Page Not Found')
        res.end()
    }
}).listen(5005, () => { console.log('Server Running') })