#!/usr/bin/node
const request = require('request');
const process = require('process');
const fs = require('fs');
const apiCall = process.argv[2];

request(apiCall, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  let jsonRes = JSON.parse(response.body);
  let userID;
  let taskNum = 0;
  let userTasks = {};

  for (dict of jsonRes) {
    userID = dict.userId;
    if (!userTasks[userID]) {
      userTasks[userID] = 0;
    }
    if (dict.completed == true)
        userTasks[userID]++;
  }

  console.log(userTasks)
});
