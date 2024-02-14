#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

function incr(number) {
    number++;
}

module.exports = {
    incr: incr
};

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
