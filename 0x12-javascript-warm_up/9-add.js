#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const argv = require('node:process').argv;
const operand1 = Number(argv[2]);
const operand2 = Number(argv[3]);
const sum = add(operand1, operand2);
console.log(`${sum}`);
