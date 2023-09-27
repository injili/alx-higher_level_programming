#!/usr/bin/node

const request = require('request');
const theUrl = process.argv[2];
request(theUrl, function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
