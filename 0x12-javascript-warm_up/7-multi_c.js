#!/usr/bin/node
const myNum = process.argv[2];
if (isNaN(parseInt(myNum))) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < myNum; count++) {
    console.log('C is fun');
  }
}
