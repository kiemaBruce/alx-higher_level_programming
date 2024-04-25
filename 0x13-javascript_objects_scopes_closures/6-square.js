#!/usr/bin/node
const SquareBase = require('./5-square');
class Square extends SquareBase {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let recSlice = '';
        for (let j = 0; j < this.width; j++) {
          recSlice += c;
        }
        console.log(recSlice);
      }
    }
  }
}
module.exports = Square;
