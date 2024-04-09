#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const numOne = parseInt(process.argv[2]);
const numTwo = parseInt(process.argv[3]);

add(numOne, numTwo);
