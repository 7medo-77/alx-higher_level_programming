#!/usr/bin/node
function add(a, b){
  console.log(a + b);
}

let numOne = parseInt(process.argv[2]);
let numTwo = parseInt(process.argv[3]);
add(numOne, numTwo);
