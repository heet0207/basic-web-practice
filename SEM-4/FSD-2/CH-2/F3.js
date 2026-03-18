let fs = require('fs')
fs.writeFile('x1.txt','Hello ',(err)=>{if(err) throw err;})
fs.appendFile('x1.txt','World !',(err)=>{if(err) throw err;})
    setTimeout(()=>{
        fs.readFile('x1.txt','utf-8',(err,data)=>{if(err) throw err;console.log(data)})
    },3000)