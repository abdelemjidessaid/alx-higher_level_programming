#!/usr/bin/node

const { argv } = require('node:process');

const len = argv.length - 2;
if (len === 0) console.log('No argument');
else if (len >= 0) console.log('Argument found');
