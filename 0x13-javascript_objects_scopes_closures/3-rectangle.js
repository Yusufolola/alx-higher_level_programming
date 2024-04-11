#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof (w) !== 'number' || w <= 0 || (typeof (h) !== 'number') || h <= 0) {
      return this;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
};
