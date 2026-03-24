let fs = require('fs');
var pm = require('path');
path = pm.dirname('LJ/Sample.txt');
console.log(path);
b = pm.basename('LJ/Sample.txt');
console.log(b);
fs.mkdirSync(path)
fs.writeFileSync(b,'Hello World !')
fs.copyFileSync(b,'copy.txt')
fs.unlinkSync(b)

