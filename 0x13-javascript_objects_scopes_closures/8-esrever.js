#!/usr/bin/node
exports.esrever = function (list) {
  let i, j = list.length - 1;
  let newArray = list.slice();

  for (i = 0; i <= j; i++, j--) {
    let tempVariable;

    tempVariable = newArray[i];
    newArray[i] = newArray[j];
    newArray[j] = tempVariable;
  }
  return (newArray);
};
