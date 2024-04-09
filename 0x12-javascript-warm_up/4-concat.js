#!/usr/bin/node
/* script that prints two arguments passed */

let arg1 = process.argv.slice(2)[0];
let arg2 = process.argv.slice(2)[1];
if (arg1 === undefined)
{
	arg1 = "undefined";
}
if (arg2 === undefined)
{
	arg2 = "undefined";
}
console.log(`${arg1} is ${arg2}`);
