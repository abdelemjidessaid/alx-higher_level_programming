#!/usr/bin/node
/**
 * script that prints all characters of a Star Wars movie
 *
 * usage:
 *  ./101-starwars_characters.js <file id>
 */

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

// print the characters
function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}

// get the data of the film
request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
