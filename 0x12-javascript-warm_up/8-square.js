#!/usr/bin/node

/**
 * A script that prints a square
 */

const size = parseInt(process.argv[2]);
let line = '';

if (isNaN(size)) {
  console.log('Missing size');
}

for (let i = 0; i < size; i++) {
  line = '';
  for (let j = 0; j < size; j++) {
    line += 'x';
  }
  console.log(line);
}
