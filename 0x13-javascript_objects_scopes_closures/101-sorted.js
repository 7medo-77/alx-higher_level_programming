#!/usr/bin/node
const dict = require('./101-data.js').dict;

function dictConstructor (dict) {
  const uniqueValues = new Set(Object.values(dict));
  const valuesArray = [...uniqueValues];
  const returnObject = {};

  for (const number of valuesArray) {
    const elementArray = [];
    for (const key in dict) {
      if (dict[key] === number) {
        elementArray.push(`${key}`);
        returnObject[`${number}`] = elementArray;
      }
    }
  }
  console.log(returnObject);
}

dictConstructor(dict);
