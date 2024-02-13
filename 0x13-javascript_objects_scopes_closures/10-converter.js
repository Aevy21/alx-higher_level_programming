#!/usr/bin/node

exports.converter = function (base) {
  return function convert (number) {
    if (number < base) {
      return '' + (number < 10 ? number : String.fromCharCode(87 + number));
    }
    return convert(Math.floor(number / base)) + (number % base < 10 ? number % base : String.fromCharCode(87 + number % base));
  };
};
