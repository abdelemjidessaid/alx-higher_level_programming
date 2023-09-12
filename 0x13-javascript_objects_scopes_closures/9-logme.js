#!/usr/bin/node

let last = 0;

// function that log the number of calls.
exports.logMe = function (item) {
  console.log(last + ': ' + item);
  last++;
};
