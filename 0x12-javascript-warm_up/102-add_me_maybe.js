#!/usr/bin/node

module.exports.addMeMaybe = function addMeMaybe (number, theFunction) {
  number++;
  theFunction (number);
};
