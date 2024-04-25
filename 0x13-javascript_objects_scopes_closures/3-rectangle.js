#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && w !== undefined && h !== undefined) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let recSlice = '';
      for (let j = 0; j < this.width; j++) {
        recSlice += 'X';
      }
      console.log(recSlice);
    }
  }
}
module.exports = Rectangle;
