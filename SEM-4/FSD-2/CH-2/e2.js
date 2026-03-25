let fs = require('fs')
let event = require('events')
const e = new event()
e.on('Write',function(){
    fs.writeFileSync('MyFile','Hello ')
    e.emit('append')
})
e.on('append',function(){
    fs.appendFileSync('MyFile','World!')
    e.emit('read')
})
e.on('read',function(){
    let x = fs.readFileSync('MyFile','utf-8')
    console.log(x)
})
e.emit('Write')