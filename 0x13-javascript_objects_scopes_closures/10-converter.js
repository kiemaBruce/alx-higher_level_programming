#!/usr/bin/node
exports.converter = function (base) {
  const myBase = base;
  return function (number) {
    return number.toString(myBase);
  };
};
