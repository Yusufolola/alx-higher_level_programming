#!/usr/bin/node

const x = process.argv.slice(2)[0];
if (isNaN(parseInt(x)))
{
	console.log("Missing number of occurrences");
}
else
{
	let i = 0;
	while (i < x)
	{
		console.log("C is fun");
		i++;
	}
}

