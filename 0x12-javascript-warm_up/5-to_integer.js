#!/usr/bin/node

if (process.argv[2]) {
  const stringOne = parseInt(process.argv[2]);
  const outputString = 'My number: ' + stringOne;
  console.log(outputString);
} else {
  console.log('Not a number');
}
