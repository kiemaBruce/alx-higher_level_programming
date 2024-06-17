#!/usr/bin/node
function factorial (num) {
  if (num === 0 || num === 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}
const myArg = process.argv[2];
const myNum = parseInt(myArg);
if (isNaN(myNum)) {
  console.log('1');
} else {
  console.log(factorial(myNum));
}
