#!/usr/bin/node

const OldSquare = require('./5-square');

// class Square advanced.
class Square extends OldSquare {
  charPrint (c) {
    const char = c || 'X';

    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) row = row + char;
      console.log(row);
    }
  }
}

module.exports = Square;
