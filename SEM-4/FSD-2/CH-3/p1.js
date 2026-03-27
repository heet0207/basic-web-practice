var pm = require('path');
path = pm.dirname('D:/LJ/FSD-2/a.html');
console.log(path);
b = pm.basename('D:/LJ/FSD-2/a.txt');
console.log(b);
ext = pm.extname('D:/LJ/FSD-2/a.txt');
console.log(ext);
var m = pm.parse('D:/LJ/FSD-2/a.html');
console.log(m)
if(ext == '.txt'){
    console.log('Text');
}
else{
    console.log('Not Text')
}