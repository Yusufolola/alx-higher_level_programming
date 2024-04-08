#!/usr/bin/node
/* a script that prints the first argument*/

if (process.agrv[2] === undefined)
{
	console.log("No argument");
}
else
{
	console.log(process.agrv[2]);
}

