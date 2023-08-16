#!/usr/bin/node

/*
 * Value of my argument
 */

const { argv } = require('node:process');

if (!process.argv[2]){
	console.log('No Argument');
}else{
	console.log(process.argv[2]);
}
