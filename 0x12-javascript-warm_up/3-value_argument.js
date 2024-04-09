#!/usr/bin/node
/* a script that prints the first argument*/

const arg = process.argv.slice(2)[0];
if (arg === undefined)
{
	console.log("No argument");
}
else{
	console.log(`${arg}`);
}

