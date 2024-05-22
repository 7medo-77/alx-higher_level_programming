#!/usr/bin/node
const request = require('request');
const process = require('process');
const websiteName = process.argv[2];

const requestLink = request.Request(websiteName)

request(websiteName, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(response.statusCode);
})
