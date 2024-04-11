#!/usr/bin/node

const square = require('./5-square');
module.exports = class Square extends square {
  charPrint (c) {
    let char = 'x';
    if (c) {
      char = c;
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(char);
      }
      process.stdout.write('\n');
    }
  }
};
