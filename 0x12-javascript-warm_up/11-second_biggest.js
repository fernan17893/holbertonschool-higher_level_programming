#!/usr/bin/node
const myVar = process.argv.length;
if (myVar <= 3) {
  console.log('0');
} else {
  process.argv.sort((a, b) => (b - a));
  console.log(process.argv[3]);
}
