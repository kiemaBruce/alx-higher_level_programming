#!/usr/bin/node
exports.esrever = function (list) {
  const lastIndex = list.length - 1;
  const newList = [];
  let j = 0;
  for (let i = lastIndex; i >= 0; i--) {
    newList[j] = list[i];
    j++;
  }
  return newList;
};
