#!/usr/bin/node

const list = require('./100-data').list;

const result = list.map((x, y) => x * y);
console.log(list);
console.log(result);
