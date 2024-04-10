#!/usr/bin/node
const myArray = [];

for (let i = 2; i < process.argv.length; i++) {
  const argNum = parseInt(process.argv[i]);
  myArray.push(argNum);
}

let maxNumber = myArray[0];
let secondMaxNumber = myArray[0];

for (const number of myArray) {
  if (number > maxNumber) {
    maxNumber = number;
  }
  if ((number >= secondMaxNumber && number < maxNumber) || (secondMaxNumber === maxNumber && number === myArray[0])) {
    secondMaxNumber = number;
  }
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(secondMaxNumber);
}
