var https = require('http')
https.createServer(function(req,res){
    res.writeHead(200,{'content-type':'application/json'})
    const data = {
                'Sub':'FSD-2',
                'Topic':'Node',
                'Teacher':'Kavan'
    }
    // res.write(JSON.stringify(data))
    // res.end()
    res.end(JSON.stringify(data))
}).listen(5001,()=>{console.log('Server Running')})