#!/usr/bin/node
const myVar = process.argv.length;
if (myVar === 3) { console.log(process.argv[2]); }
if (myVar < 3) { console.log("No argument"); }
