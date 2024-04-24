#!/usr/bin/node
/**
 * countGreater - counts the distinct elements that are greater than x in an array.
 * @x: the element in the array to be checked.
 * @arr: the array in which x is to be checked.
 * Description: the function isn't completely accurate: the first array element
 * with repeated values won't be counted for each other element with the same
 * value. But if more than one elements are repeated, then the subsequent
 * elements are counted for the second and other repeated elements. That is, the
 * function only keeps track of one of the elements with repeated elements to
 * ensure that the repeated ones aren't added to no, but subsequent elements
 * aren't monitored and as such their repeated values may be added to no. But
 * that behaviour doesn't impede the function and it still accomplishes it's
 * goal in this limited scope and context.
 * Return: the number of distinct elements that have a value greater than x in
 * array arr.
 */
function countGreater (x, arr) {
  let no = 0;
  let lastGreatest;

  for (let i = 2; i < arr.length; i++) {
    if (Number(arr[i]) > Number(x)) {
      if (no === 0) {
        lastGreatest = arr[i];
        no += 1;
      } else if (arr[i] !== lastGreatest) {
        no += 1;
      }
    }
  }
  return no;
}
const argv = require('node:process').argv;
if (argv.length < 4) {
  console.log(0);
} else {
  let i = 2;
  let r = 0;
  while (argv[i]) {
    if (countGreater(argv[i], argv) === 1) {
      r = argv[i];
      break;
    }
    i += 1;
  }
  console.log(`${r}`);
}
