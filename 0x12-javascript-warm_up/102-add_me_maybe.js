#!/usr/bin/node

const addMeMaybe = function addMeMaybe (number, theFunction) {
  number++;
  theFunction (number);
};

module.exports = {
  addMeMaybe: addMeMaybe
};
