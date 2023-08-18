#!/usr/bin/node

/*
 * A script that prints the addition of 2 integers
 */

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(first, second));
