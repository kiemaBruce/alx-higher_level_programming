#!/usr/bin/node
const argv = require('node:process').argv;
const size = Number(argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  if (size !== 0) {
    for (let i = 0; i < size; i++) {
      let lineStr = 'X';
      for (let j = 1; j < size; j++) {
        lineStr += 'X';
      }
      console.log(lineStr);
    }
  }
}
