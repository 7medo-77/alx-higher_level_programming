#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const file_name = process.argv[2];
const data = process.argv[3];

fs.writeFile(file_name, data,'utf-8', (err) => {
  if (err) {
    console.log(err);
    return;
  }
});
