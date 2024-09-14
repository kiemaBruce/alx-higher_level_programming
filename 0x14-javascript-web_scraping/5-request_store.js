#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    /* Write to the file asynchronously */
    fs.writeFile(filePath, body, function (err) {
      if (err) {
        console.error(err);
      }
    });
  } else if (error) {
    /* Network related or low-level errors */
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.log(`code: ${response.statusCode}`);
  }
});
