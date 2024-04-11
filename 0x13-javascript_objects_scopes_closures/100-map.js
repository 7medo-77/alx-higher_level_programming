#!/usr/bin/node
let list = require('./100-data.js').list;

let newArray = list.map((num, idx) => num * idx);

console.log(list);
console.log(newArray);
