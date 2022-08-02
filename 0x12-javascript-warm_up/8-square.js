#!/usr/bin/node
const num = process.argv[2];
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
}
for (let i = 0; i < num; i++) {
  let row = '';
  for (let j = 0; j < num; j++) {
    row += '#';
  }
  console.log(row + ' ');
}
