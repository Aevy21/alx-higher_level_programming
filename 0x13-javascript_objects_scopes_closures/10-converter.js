#!/usr/bin/node

exports.converter = function (base) {
  return function convert (number) {
    if (number < base) {
      return '' + number;
    }
    return convert(Math.floor(number / base)) + (number % base);
  };
};
