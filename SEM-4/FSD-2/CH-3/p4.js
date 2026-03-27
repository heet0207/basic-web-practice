let fs = require('fs')
let v = require('url')
process.noDeprecation=true
var addr = 'http://localhost:8080/default.html ?m1=50&m2=60&m3=70'
let x = v.parse(addr,true)
let m1 = parseInt(x.query.m1)
let m2 = parseInt(x.query.m2)
let m3 = parseInt(x.query.m3)
console.log(m1,m2,m3)
let sum = m1+ m2 + m3
console.log(sum)
let avg = sum/3
console.log('Avg  of Sum :',avg)