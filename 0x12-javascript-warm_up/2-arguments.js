#!/usr/bin/node

/*
 * A script that takes in arguments giving a report on the count
 */

const count = process.argv.length - 2;

if (count === 0) {
  console.log('No argument');
} else if (count === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
