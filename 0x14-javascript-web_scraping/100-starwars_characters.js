#!/usr/bin/node
/*
    script that prints all characters of a film
    using its id.

    usage:
        ./100-starwars_characters.js <film id>
*/
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

// print the character names
function printCharacters (characters) {
  characters.forEach(char => {
    request(char, function (err, res, body) {
      if (!err) {
        const name = JSON.parse(body).name;
        console.log(name);
      }
    });
  });
}

// get the character urls
request(url, function (err, res, body) {
  if (!err) {
    const data = JSON.parse(body);
    printCharacters(data.characters);
  }
});
