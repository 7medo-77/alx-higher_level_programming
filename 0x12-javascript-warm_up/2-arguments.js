#!/usr/bin/node
const printOutput = process.argv.length === 3 ? 'Argument found' : 'Arguments found';

if (process.argv.length >= 3) {
  console.log(printOutput);
} else {
  console.log('No argument');
}
