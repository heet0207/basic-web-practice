var https = require('http')
https.createServer(function(req,res){
    res.writeHead(200,{'content-type':'text/html'})
    res.write('<h1> Hello World </h1>')
    res.write('I Am a Devil')
    res.end()
}).listen(5000,()=>{console.log('Server Running')})