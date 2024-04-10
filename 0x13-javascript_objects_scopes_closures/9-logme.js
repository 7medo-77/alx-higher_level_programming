#!/usr/bin/node
const logObject = {};

exports.logMe = function (item) {
  let myArray = Object.keys(logObject)
  const lastNum = myArray.length;

  if (myArray.length === 0){
    logObject[`${lastNum}`] = item;
  } else {
    logObject[`${lastNum}`] = item;
  }
  console.log(`${lastNum}: ${item}`);
}
