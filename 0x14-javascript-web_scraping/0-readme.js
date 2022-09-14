#!/usr/bin/node
/* read and print contents of file */

const srcFile = process.argv[2];
const fs = require('fs');

fs.readFile(srcFile, 'utf8', function (err, data) {
  if (err) throw err;

  console.log(data.toString());
});
