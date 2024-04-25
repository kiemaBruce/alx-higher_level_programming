#!/usr/bin/node
exports.logMe = (function (item) {
  let logCount = 0;
  return (myItem) => {
    console.log(`${logCount}: ${myItem}`);
    logCount += 1;
  };
})();
