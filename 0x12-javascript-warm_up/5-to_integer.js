#!/usr/bin/node
/* a script that prints first arg converted to int */

const num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
