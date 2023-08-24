#!/usr/bin/node

/*
 * Draw the rectangle using x.
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let arr = {};
      for (let j = 0; j < this.width; j++) {
        arr += 'x';
      }
      console.log(arr);
    }
  }
}

module.exports = Rectangle;
