#!/usr/bin/node
exports.converter = function (base) {
  return ((param) => {
    return (param.toString(base))
  })
}
