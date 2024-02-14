#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

const incr = {
    incr: function(number) {
        return number + 1;
    }
};

module.exports = incr;

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
