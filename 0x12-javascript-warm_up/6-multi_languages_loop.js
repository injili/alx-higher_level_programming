#!/usr/bin/node

/*
 * Print an output using a loop.
 */

const theMessage = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (const i in theMessage) {
  console.log(theMessage[i]);
}
