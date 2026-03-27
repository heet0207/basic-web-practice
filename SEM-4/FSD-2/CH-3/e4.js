let fs = require('fs')
let event = require('events')
const e = new event()
var f=(msg)=>{
    console.log(msg)
}
var f1=(msg)=>{console.log(msg)}
    e.on('My Event1',f)
    e.on('My Event2',f1)
    e.on('My Event1',f)
    e.on('My Event2',f1)


e.removeListener('My Event2',f1)
e.removeAllListeners('My Event1')
e.emit('My Event2','LJU')
e.emit('My Event1','LJKU')