let fs = require('fs')

fs.writeFileSync('CSD.txt', '');
fs.appendFileSync('CSD.txt','Hello World');
let data = fs.readFileSync('CSD.txt','utf-8');
fs.renameSync('CSD.txt','ir.txt');
console.log(data);