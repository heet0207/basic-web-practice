let fs = require('fs')
// fs.writeFileSync('q1.txt','1,2,3,4,5,6,7,8,9,10')
// let x = fs.readFileSync('q1.txt','utf-8')
// let b = x.split(',')
// let s = b.sort((a,b)=>a-b)
// console.log(s)


fs.writeFile('q2.txt','1,2,3,4,5',(err)=>{if(err) throw err;})
fs.readFile('q2.txt','utf-8',(err,data)=>{if(err) throw err;
    console.log(data);
let w =data.split(',').sort((a,b)=>a-b)
console.log(w)})
