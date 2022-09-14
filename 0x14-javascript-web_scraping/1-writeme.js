#!/usr/bin/node
/* Script writes string to a file */

const fs = require('fs');

const data = process.argv[3];

fs.writeFile(process.argv[2], data, (err) => {
  if (err) throw err;
});
