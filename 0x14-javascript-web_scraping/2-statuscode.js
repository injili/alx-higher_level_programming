#!/usr/bin/node

const request = require('request');
const theUrl = process.argv[2];
request(theUrl, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code: ', response && response.statusCode);
});
