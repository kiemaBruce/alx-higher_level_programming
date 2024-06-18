#!/usr/bin/node
exports.esrever = function (list) {
  const retList = [];
  let i = list.length - 1;
  for (let j = 0; j < list.length; j++) {
    retList[j] = list[i];
    i--;
  }
  return (retList);
};
