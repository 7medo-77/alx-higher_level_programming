#!/usr/bin/node
const SquareParent = require('./5-square.js');

class Square extends SquareParent {
  constructor(size) {
    super(size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let printArray = '';
      for (let j = 0; j < this.width; j++) {
        printArray += c ? 'C' : 'X';
      }
      console.log(printArray);
    }
  }

}
module.exports = Square;
