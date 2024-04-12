#!/usr/bin/node
const fs = require('fs');
let contentFile1='';
let contentFile2='';

function readFileFunction (callback) {
  fs.readFile(process.argv[2], (err, data) => {
    callback(null, data.toString())
  })
};
readFileFunction((err, content) => {
  contentFile1 = content;
})
console.log(contentFile1)

fs.readFile(process.argv[3], (err, data) => {
  contentFile2 = data.toString();
});
console.log(contentFile2)

// fs.writeFile(process.argv[2], contentFile1 + contentFile2, 'a', (err) => {
//   if (err) {
//     console.error(err);
//   }
// });
