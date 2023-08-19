#!/usr/bin/node

/*
 * A script that searches the second biggest integer in the list of arguments
 */

const theArray = process.argv.slice(2);

function findSecond (arr) {
  if (arr.length < 2) {
    return 0;
  }
  arr.sort((x, y) => y - x);
  return arr[1];
}

console.log(findSecond(theArray));
