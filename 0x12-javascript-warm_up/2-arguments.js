#!/usr/bin/node
const myVar = process.argv.length;
if (myVar === 2) { console.log('No argument'); }
if (myVar === 3) { console.log('Argument found'); }
if (myVar > 3) { console.log('Arguments found'); }
