#!/usr/bin/node
let myArray = [];

for (let i = 2; i < process.argv.length; i++){
  let arg_num = parseInt(process.argv[i]);
  myArray.push(arg_num);
}

let maxNumber = myArray[0];
let secondMaxNumber = myArray[0];

for (let number of myArray){
  if (number > maxNumber){
    maxNumber = number;
  }
  if (number > secondMaxNumber && number < maxNumber || secondMaxNumber == maxNumber){
    secondMaxNumber = number;
  }
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(secondMaxNumber);
}
