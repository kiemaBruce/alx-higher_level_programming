#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const tasksArray = JSON.parse(body);
    let userId = null;
    const userTasks = {};
    let completed = 0;
    let prevUserId = null;
    for (const task of tasksArray) {
      if (task.userId !== prevUserId) {
        completed = 0;
      }
      if (task.completed) {
        completed++;
      }
      userId = task.userId;
      userTasks[userId] = completed;
      prevUserId = userId;
    }
    // Remove users with no completed tasks.
    const filteredUserTasks = {};
    for (const user in userTasks) {
      if (userTasks[user] !== 0) {
        filteredUserTasks[user] = userTasks[user];
      }
    }
    console.log(filteredUserTasks);
  } else if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.log(`code: ${response.statusCode}`);
  }
});
