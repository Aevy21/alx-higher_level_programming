#!/usr/bin/node

const list = require('./100-data.js');

const newList = list.map((value, index) => value * index);
