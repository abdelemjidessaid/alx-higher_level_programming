#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';
const character = 'https://swapi-api.alx-tools.com/api/people/18/';
request(url, function (err, res, body) {
  if (res.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;
    for (i = 0; i < data.results.length; i++) {
      if (data.results[i].characters.includes(character)) {
        count++;
      }
    }
    console.log(count);
  } else {
    console.error(err);
  }
});
