#!/usr/bin/node
/* script that prints two arguments passed */

const arg1 = process.argv.slice(2)[0];
const arg2 = process.argv.slice(2)[1];
console.log(`${arg1} is ${arg2}`);
