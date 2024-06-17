#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const argsArr = process.argv.slice(2);
  const myArr = [];
  for (let count = 0; count < argsArr.length; count++) {
    myArr[count] = parseInt(argsArr[count]);
  }
  let count = 0;
  let largest = myArr[0];
  /* First get the largest */
  while (myArr[count]) {
    if (myArr[count] > largest) {
      largest = myArr[count];
    }
    count++;
  }
  /* Then get the second largest */
  /* Assign secondLargest to any value other than largest */
  let secondLargest;
  for (let num = 0; num < myArr.length; num++) {
    if (myArr[num] !== largest) {
      secondLargest = myArr[num];
      break;
    }
  }
  /* Then iterate through entire array to get actual 2nd largest */
  count = 0;
  while (myArr[count]) {
    if (myArr[count] < largest && myArr[count] > secondLargest) {
      secondLargest = myArr[count];
    }
    count++;
  }
  console.log(secondLargest);
}
