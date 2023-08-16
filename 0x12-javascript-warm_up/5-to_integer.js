#!/usr/bin/node

/*
 * Output the integer argument.
 */

if (!isNaN(parseInt(process.argv[2]))) {
  console.log('My number : ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
