#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';
request(url, function (err, res, body) {
  if (res.statusCode === 200) {
    const data = JSON.parse(body).results;
    console.log(data.reduce((count, film) => {
      return film.characters.find((character) => character.endsWith('18/'))
      ? count + 1 : count;
    }, 0));
  }
});
