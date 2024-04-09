#!/usr/bin/node

class Rectangle{
}
if (require.main === module) { // Check if the file is the main module
  const r1 = new Rectangle();
  console.log(r1);
  console.log(r1.constructor);
}
