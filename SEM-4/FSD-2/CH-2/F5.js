let data = [{'Name': 'John', 'Age': 25},
            {'Name': 'Jane', 'Age': 30},
            {'Name': 'Doe', 'Age': 35}];
let fs = require('fs');
let jsonData = JSON.stringify(data);
fs.writeFileSync('Student.txt', jsonData);
let x = fs.readFileSync('Student.txt','utf-8')
console.log(x);