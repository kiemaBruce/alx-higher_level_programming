#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const filmObj = JSON.parse(body);
    const characters = filmObj.characters;
    for (const characterUrl of characters) {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterObj = JSON.parse(body);
          const characterName = characterObj.name;
          console.log(characterName);
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
