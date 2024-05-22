#!/usr/bin/node
const request = require('request');
const process = require('process');
const apiCall = process.argv[2];
const wedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/' + '18/';

request(apiCall, (error, response, body) => {
  if (error) {
    console.log(response.error);
  }

  let num = 0;
  const jsonReply = JSON.parse(response.body);
  for (const res of jsonReply.results) {
    if (res.characters.find(character => character === wedgeAntilles)) {
      num++;
    }
  }

  console.log(num);
});
