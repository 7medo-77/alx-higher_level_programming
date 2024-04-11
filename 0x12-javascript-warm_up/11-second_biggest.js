#!/usr/bin/node
const myArray = [];

for (let i = 2; i < process.argv.length; i++) {
  const argNum = parseInt(process.argv[i]);
  myArray.push(argNum);
}

let maxNumber = Number.MIN_SAFE_INTEGER;
let secondMaxNumber = Number.MIN_SAFE_INTEGER;

for (let i = 0; i < myArray.length; i++) {
  if (myArray[i] > maxNumber) {
    maxNumber = myArray[i];
  }
  if ((myArray[i] > secondMaxNumber && myArray[i] < maxNumber) || (myArray[i - 1] > secondMaxNumber && myArray[i - 1] < maxNumber)) {
    if (!myArray[i + 1]) {
      secondMaxNumber = myArray[i] >= myArray[i - 1] ? myArray[i] : myArray[i - 1];
    } else {
      secondMaxNumber = myArray[i] >= myArray[i - 1] ? myArray[i - 1] : myArray[i];
    }
  }
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(secondMaxNumber);
}
