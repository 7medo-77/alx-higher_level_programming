#!/usr/bin/node
let string_1 = process.argv[2] ? process.argv[2] : 'undefined';
let string_2 = process.argv[3] ? process.argv[3] : 'undefined';
let outputString = string_1 + ' is ' + string_2;

console.log(outputString);
