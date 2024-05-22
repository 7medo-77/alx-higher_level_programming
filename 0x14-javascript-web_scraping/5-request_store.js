#!/usr/bin/node
const request = require('request');
const process = require('process');
const fs = require('fs');
const apiCall = process.argv[2];
const filePath = process.argv[3];

request(apiCall).pipe(fs.createWriteStream(filePath, 'utf-8', (err) => {
  if (err) {
    console.err(err);
  }
}));
