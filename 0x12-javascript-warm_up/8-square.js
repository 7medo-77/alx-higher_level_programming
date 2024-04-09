#!/usr/bin/node
const numberIterations = parseInt(process.argv[2]);
let i = 0;
let mySentence = 'X';

if (numberIterations) {
  for (i = 0; i < numberIterations; i++) {
    mySentence = 'X';
    for (let j = 0; j < (numberIterations - 1); j++) {
      mySentence += 'X';
    }
    console.log(mySentence);
  }
} else {
  console.log('Missing number of occurrences');
}
