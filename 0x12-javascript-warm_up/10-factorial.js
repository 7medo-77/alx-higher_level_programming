#!/usr/bin/node
function factorial (a) {
  if (a === 1 || !a) {
    return (1);
  }
  return (a * factorial(a - 1));
}

const numOne = parseInt(process.argv[2]);
const number = factorial(numOne);

console.log(number);
