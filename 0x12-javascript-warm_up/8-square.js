#!/usr/bin/node
/* a script that prints a square*/

let size = process.argv.slice(2)[0];
if (Number.isNaN(parseInt(size)))
{
	console.log("Missing size");
}
for (let i = 0; i < size; i++)
{
	for (let j = 0; j < size; j++)
	{
		process.stdout.write("X");
	}
	console.log()
}
