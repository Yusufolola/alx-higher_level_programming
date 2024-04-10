#!/usr/bin/node
const firstarg = Number(process.argv[2]);
const secondarg = Number(process.argv[3]);
function add(a, b) {
	
	return (a + b);
}
console.log(add(firstarg, secondarg));
