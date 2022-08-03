#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
let counter = 0;

for (item of list.length) {
	if (item == searchElement) {
	counter++;
	}
  };
	console.log(counter);
};
