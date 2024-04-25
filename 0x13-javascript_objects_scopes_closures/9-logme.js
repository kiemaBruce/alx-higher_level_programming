#!/usr/bin/node
exports.logMe = (function (item) {
  let logCount = 0;
  return (item) => {
    console.log(`${logCount}: ${item}`);
    logCount += 1;
  };
})();
