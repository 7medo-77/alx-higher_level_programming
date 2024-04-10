#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  let j;
  let newArray = list;

  for (i = 0, j = newArray.length - 1; i >= j; i++, j--) {
    let tempVariable;

    tempVariable = newArray[i];
    newArray[i] = list[j];
    newArray[j] = tempVariable;
  }
  return (newArray);
};
