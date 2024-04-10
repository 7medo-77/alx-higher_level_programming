#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w && h) && (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let printArray = '';
      for (let j = 0; j < this.width; j++) {
        printArray += 'X';
      }
      console.log(printArray);
    }
  }
}
module.exports = Rectangle;
