#!/usr/bin/node

const executeXTimes = function(x, theFunction) {
    for (let i = 0; i < x; i++) {
        theFunction(); // C
    }
};
module.exports = executeXTimes;
