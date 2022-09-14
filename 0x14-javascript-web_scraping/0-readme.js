#!/usr/bin/node
/* read and print contents of file */

let srcFile = process.argv[2];
const fs = require('fs');

const file = fs.readFile(srcFile, 'utf8', function(err, data){

    console.log(data);
});
