#!/usr/bin/node
const myArg = process.argv[2];
if (isNaN(parseInt(myArg))) {
  console.log('Missing size');
} else {
  const size = parseInt(myArg);
  for (let height = 0; height < size; height++) {
    let myStr = '';
    for (let width = 0; width < size; width++) {
      myStr += 'X';
    }
    console.log(myStr);
  }
}
