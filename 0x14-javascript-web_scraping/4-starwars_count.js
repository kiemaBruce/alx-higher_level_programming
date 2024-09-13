#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const compUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const decodedInfo = JSON.parse(body);
    const noOfFilms = decodedInfo.count;
    const filmsInfo = decodedInfo.results;
    let filmsActed = 0;
    for (let i = 0; i < noOfFilms; i++) {
      const currentFilm = filmsInfo[i];
      for (const characterUrl of currentFilm.characters) {
        if (characterUrl === compUrl) {
          filmsActed += 1;
        }
      }
    }
    console.log(filmsActed);
  } else {
    console.log(error);
  }
});
