#!/usr/bin/node
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      let sz = '';
      for (let i = 0; i < this.width; i++) {
        sz += String(c);
      }
      for (let j = 0; j < this.height; j++) {
        console.log(sz);
      }
    } else {
      this.print();
    }
  }
};
