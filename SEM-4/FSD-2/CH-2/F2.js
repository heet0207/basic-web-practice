let fs = require('fs')

fs.writeFile("s3.txt","Hello",(err)=>{if(err)throw err;
    else{fs.appendFile("s3.txt"," World",(err)=>{if(err)throw err;
        else{fs.readFile("s3.txt",'utf-8',(err,data)=>{if(err)throw err;else console.log(data)})}})}})
