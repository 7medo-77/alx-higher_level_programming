#!/usr/bin/node
const stringOne = process.argv[2] ? process.argv[2] : 'undefined';
const stringTwo = process.argv[3] ? process.argv[3] : 'undefined';
const outputString = stringOne + ' is ' + stringTwo;

console.log(outputString);
