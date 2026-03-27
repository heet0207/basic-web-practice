const event = require('events')
const e = new event()

e.on('Connection',function(){
    console.log('Print Connection Successfully')
    e.emit('Data Received')
})
e.on('Data Received',function(){
        console.log('Data Received Successfully')
    })
e.emit('Connection')

