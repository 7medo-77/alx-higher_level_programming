#!/usr/bin/node
exports.esrever = function (list) {
  const newList = list.reverse();
  list.reverse();
  return (newList);
};
