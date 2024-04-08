#!/usr/bin/node
/* script that prints two arguments passed */

if (process.argv.length <= 1)
{
	console.log("undefined is undefined");
}
else if (process.argv.length <= 2)
{
	console.log(`${process.argv[2]} is undefined`);
}
else
{
	console.log(`${process.argv[2]} is ${process.argv[3]}`);
}
