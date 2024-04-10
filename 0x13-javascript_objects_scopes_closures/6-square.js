#!/usr/bin/node
const SquareParent = require('./5-square.js');

class Square extends SquareParent {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let printArray = '';
      for (let j = 0; j < this.width; j++) {
        printArray += !c ? 'X' : c;
      }
      console.log(printArray);
    }
  }
}
module.exports = Square;
