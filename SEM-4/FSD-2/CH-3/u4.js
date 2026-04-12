var https = require('http')
https.createServer(function(req,res){
    
    if(req.url=='/'){
        res.writeHead(200,{'content-type':'text/html'})
        res.write(`<ul><li><a href="/">Home</a></li><li> <a href="/about">About</a></li></ul>`)
        res.write(`<ul><li> <a href="/ab">Ab</a></li></ul>`)
        res.end()
    }
    else if(req.url=="/about"){
        res.writeHead(200,{'content-type':'text/html'})
        res.write('This Is About Us Page')
    }
    else{
        res.writeHead(404,{'content-type':'text/html'})
        res.write('Page Not Found')
        res.end()
    }
}).listen(5004,()=>{console.log('Server Running')})

