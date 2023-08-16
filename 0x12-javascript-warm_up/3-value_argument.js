#!/usr/bin/node

/*
 * Value of my argument
 */

if (!process.argv[2]) {
  console.log('No Argument');
} else {
  console.log(process.argv[2]);
}
