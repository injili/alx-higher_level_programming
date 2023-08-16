#!/usr/bin/node

/*
 * A script that prints "C is fun" as many times as possible.
 */

const times = parseInt(process.argv[2]);

if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else if (times > 0) {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
