#!/usr/bin/node
function recursiveFactorial (a) {
  if (a === 1) {
    return 1;
  }
  return a * recursiveFactorial(a - 1);
}
const argv = require('node:process').argv;
const no = Number(argv[2]);
if (isNaN(no)) {
  console.log(1);
} else {
  console.log(`${recursiveFactorial(no)}`);
}
