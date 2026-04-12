var fs = require('fs')
var u = require('url')
process.noDeprecation=true
var add = 'https://www.google.com/exam.txt?c1=Hello&c2=FSD-2+T1+Test&c3=Welcome'
let x = u.parse(add,true)
let c1 = (x.query.c1)
let c2 = (x.query.c2)
let c3 = (x.query.c3)
let sum = c1 +'\n'+c2+'\n'+c3
const filename = '.' + x.pathname
fs.writeFileSync(filename,sum)
var https = require('http')
https.createServer(function(req,res){
    if (req.url == '/') {
        fs.readFile(filename,'utf-8', (err,data) => {
                    if (err) {
                        res.writeHead(404)
                        res.end()
                    } else {
                        res.writeHead(200, { 'Content-Type': 'text/plain' });
                        res.end(data)
                    }
                });
        res.end();
    }
    else {
        res.writeHead(404, { 'content-type': 'text/html' })
        res.write('Page Not Found')
        res.end()
    }
}).listen(5006)