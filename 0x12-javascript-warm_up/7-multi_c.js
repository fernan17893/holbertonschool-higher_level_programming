#!/usr/bin/node
const num = process.argv[2];
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
}
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
