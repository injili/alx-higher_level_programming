#!/usr/bin/node

const url = process.argv[2];
const filename = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, (error, response, body) => {
  if (error == null) {
    fs.writeFileSync(bodyResp, body);
  }
});
