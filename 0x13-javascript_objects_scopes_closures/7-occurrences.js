#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let repArray = [];

  for (const num of list) {
    if (num === searchElement) {
      repArray.push(1);
    }
  }
  return (repArray.length);
}
