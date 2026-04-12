var https = require('http')
https.createServer(function(req,res){
    res.writeHead(200,{'content-type':'text/html'})
    res.write(req.url)
    res.end()
}).listen(5002,()=>{console.log('Server Running')})