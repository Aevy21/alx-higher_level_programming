#!/usr/bin/node

exports.logMe = function (item) {
  if (typeof exports.logMe.counter === 'undefined') {
    exports.logMe.counter = 0;
  }
  console.log(exports.logMe.counter + ': ' + item);
  exports.logMe.counter++;
};
