#!/usr/bin/node
const addMeMaybe = {
  addMeMaybe (number, theFunction) {
    let i = 0;
    let nb = 1;
    while (i < number) {
      nb++;
      i++;
      theFunction();
    }
  }
};
module.exports = addMeMaybe;
