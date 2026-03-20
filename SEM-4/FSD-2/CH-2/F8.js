const s = {d:{'a':10,'b':20},'c':[30,10]};
let fs = require('fs');
let jd = JSON.stringify(s);
fs.writeFileSync('s2.txt', jd);
let r = fs.readFileSync('s2.txt','utf-8')
    let x = JSON.parse(r);
    let z =x.d.a;
    let q =x.d.b;
    let p =x.c[0];
    let e =x.c[1];
    let sum = z + q;
    let sub = e - q;
    let mul = p * z;
fs.appendFileSync('s2.txt','\nSum :'+sum + '\nSub :'+sub + '\nMul :'+mul);
console.log('Sum :'+sum);
console.log('Sub :'+sub);
console.log('Mul :'+mul);
