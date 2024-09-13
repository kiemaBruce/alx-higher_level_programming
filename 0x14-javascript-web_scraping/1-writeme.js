#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const str = process.argv[3];
try {
  fs.writeFileSync(filePath, str, 'utf-8');
} catch (err) {
  console.log(err);
}
