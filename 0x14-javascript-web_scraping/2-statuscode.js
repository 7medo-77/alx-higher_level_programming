#!/usr/bin/node
const request = require('request');
const process = require('process');
const websiteName = process.argv[2];

request(websiteName, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log("code:", response.statusCode);
})
