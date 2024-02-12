#!/usr/bin/nodejs

const firstArgument = process.argv[2];
const integerNumber = parseInt(firstArgument, 10);

if (!isNaN(integerNumber)) {
  console.log('My number: ' + integerNumber);
} else {
  console.log('Not a number');
}
