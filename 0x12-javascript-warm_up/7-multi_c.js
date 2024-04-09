#!/usr/bin/node
const numberIterations = parseInt(process.argv[2]);
let i = 0;
const mySentence = 'C is fun';

if (numberIterations) {
  for (i = 0; i < numberIterations; i++) {
    console.log(mySentence);
  }
} else {
  console.log('Missing number of occurrences');
}
