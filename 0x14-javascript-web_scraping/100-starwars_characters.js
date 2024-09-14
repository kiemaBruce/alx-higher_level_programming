#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
let completedRequests = 0;
const charactersObj = {};
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const filmObj = JSON.parse(body);
    const characters = filmObj.characters;
    for (const characterUrl of characters) {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const index = parseInt(characterUrl.split('https://swapi-api.alx-tools.com/api/people/')[1].slice(0, -1));
          const characterName = JSON.parse(body).name;
          if (characterName) {
            charactersObj[index] = characterName;
          }
          completedRequests++;
          if (completedRequests === characters.length) {
            for (const character in charactersObj) {
              console.log(charactersObj[character]);
            }
          }
        } else if (error) {
          console.error(error);
        } else if (response.statusCode !== 200) {
          console.log(`code: ${response.statusCode}`);
        }
      });
    }
  } else if (error) {
    /* Network related or low-level errors */
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.log(`code: ${response.statusCode}`);
  }
});
