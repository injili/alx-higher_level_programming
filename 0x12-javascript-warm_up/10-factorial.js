#!/usr/bin/node

/*
 * A script that computes and prints a factorial
 */

const a = parseInt(process.argv[2]);

function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

if (a === 1 || isNaN(a)) {
  console.log('1');
} else {
  console.log(factorial(a));
}
