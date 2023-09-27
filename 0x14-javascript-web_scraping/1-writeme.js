#!/usr/bin/node

const fs = require('fs');
const  filename = process.argv[2];
const whatToWrite = process.argv[3];

fs.writeFile(filename, whatToWrite, 'utf8', (err) => {
	if (err) {
		console.log(err);
		return;
	}
})
