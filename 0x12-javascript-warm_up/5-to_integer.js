#!/usr/bin/node
/* a script that prints first arg converted to int */

let num = process.argv[2];
if (isNaN(parseInt(num)))
{
	console.log("Not a number");
}
else
{
	console.log(`My number: ${parseInt(num)}`);
}
