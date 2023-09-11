#!/usr/bin/node

const { argv } = require('node:process');

const len = argv.length - 2;
console.log(
    count === 2
        ? 'No argument'
        : count === 3
        ? 'Argument found'
        : 'Arguments found'
);
