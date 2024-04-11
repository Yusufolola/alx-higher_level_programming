#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let nb = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      nb += 1;
    }
    i++;
  }
  return nb;
};
