#!/usr/bin/node
const request = require('request');
const process = require('process');
const apiCall = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const movieID = process.argv[2];

request(apiCall, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const jsonResult = JSON.parse(response.body);

  async function getCharacters(result){
    let characterList = [];
    for (const character of jsonResult.characters) {
        const requestURL = character.toString();
        await request(requestURL, (error, response, body) => {
          if (error) {
            console.error(error);
          }
          const characterJson = JSON.parse(response.body);
          characterList.push(characterJson.name);
          console.log(characterList[characterList.length-1])
        });
    }
  }
  getCharacters(jsonResult);
});
