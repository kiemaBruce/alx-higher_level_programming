#!/usr/bin/node
const SquareOrig = require('./5-square.js');
class Square extends SquareOrig {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let myStr = '';
      for (let j = 0; j < this.width; j++) {
        myStr += c;
      }
      console.log(myStr);
    }
  }
}
module.exports = Square;
