const Shape = [
        {'Name':'Circle','Diameter':8},
        {'Name':'Square','Side':10}]
let fs = require('fs');
let jd = JSON.stringify(Shape);
fs.writeFileSync('Shape.txt', jd);
fs.readFileSync('Shape.txt','utf-8')
    let x = Shape[0].Diameter;
    let y = Shape[1].Side;
    let circle = 2*3.14*(x/2);
    let square = 4*y;
    console.log('Perimeter of Circle: '+circle);
    console.log('Perimeter of Square: '+square);
fs.appendFileSync('Shape.txt', '\nPerimeter of Circle: '+circle);
fs.appendFileSync('Shape.txt', '\nPerimeter of Square: '+square);
