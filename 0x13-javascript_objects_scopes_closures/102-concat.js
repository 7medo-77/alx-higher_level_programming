#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], (err, data) => {
  const contentFile1 = data.toString();
});

fs.readFile(process.argv[3], (err, data) => {
  const contentFile2 = data.toString();
});

fs.writeFile(process.argv[2], contentFile2 + contentFile2, 'a', (err) => {
  if (err) {
    console.error(err);
  }
});
