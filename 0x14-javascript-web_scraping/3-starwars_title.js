#!/usr/bin/node
const request = require('request');
const process = require('process');
const apiCall = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(apiCall, (error, response, body) => {
  if (error) {
    console.log(response.error);
  }
  const jsonReply = JSON.parse(response.body);
  console.log(jsonReply.title);
});
