let fs = require('fs')
let v = require('url')
process.noDeprecation=true
var addr = 'http://localhost:8080/default.html ?year=2025&month=Feb'
let x = v.parse(addr,true)
 console.log(x)
// fs.writeFileSync('z.txt',JSON.stringify(x))
// console.log(fs.readFileSync('z.txt','utf-8'))
// console.log(x.query.year)
// console.log(x.query.month)
// if(x.query.year % 4 ==0){
//     console.log('Leap')
// }
// else{
//     console.log('Not Leap')
// }