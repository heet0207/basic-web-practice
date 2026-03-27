let fs = require('fs')
let event = require('events')
const e = new event()

e.on('perimeter',(a,b)=>{
    if (a < 0){
        console.log('Radius Must Be Positive')
    }
    else{
        p = 2*3.14*a
        console.log('Circle Perimeter :',p)
    }
    if (b < 0){
        console.log('Side Must Be Positive')
    }
    else{
        x = 4*b
        console.log('Square Perimeter :',x)
    }
})
e.emit('perimeter',1,10)