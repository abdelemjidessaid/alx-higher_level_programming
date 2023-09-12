#!/usr/bin/node

// function that converts numbers to a specific base.
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
