const Student = [
    {'Name': 'Kavan','Age': 20},
    {'Name': 'Heet','Age': 22},
    {'Name': 'Megh','Age': 22}
]
let fs = require('fs');
let jd = JSON.stringify(Student);
fs.writeFileSync('Student.txt', jd);
let d = fs.readFileSync('Student.txt','utf-8')
let x  = JSON.parse(d);
console.log(x);