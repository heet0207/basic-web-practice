let fs = require('fs')
let event = require('events')
const e = new event()

var f=(msg)=>{console.log(msg)}
var f1=(msg)=>{console.log(msg)}
e.on('my',f)
e.on('my',f)
e.emit('my')
e.removeListener('my')
e.emit('my')