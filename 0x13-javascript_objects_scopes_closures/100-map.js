#!/usr/bin/node
const list = require('./100-data.js').list;
const newArray = list.map((num, idx) => num * idx);

console.log(list);
console.log(newArray);
