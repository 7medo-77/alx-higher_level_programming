#!/usr/bin/node

if (process.argv[2]) {
  const stringOne = parseInt(process.argv[2]);
  const outputString = stringOne ? 'My number: ' + stringOne : 'Not a number';
  console.log(outputString);
} else {
  console.log('Not a number');
}
