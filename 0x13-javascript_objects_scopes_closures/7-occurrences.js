#!/usr/bin/node
exports.nbOccurences = (list, searchElement) =>
  list.filter((element) => (element === searchElement)).length;