#!/usr/bin/node
let a = 100;

function add() {
  console.log(a + 15);
  function more(){
    let b = 22;
    console.log(a);
    console.log(b);
  }
  console.log(b);
  more();
}

add();
