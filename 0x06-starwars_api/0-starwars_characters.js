#!/usr/bin/node
/*
get Star Wars characters from the Star Wars API
 */

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

if (isNaN(process.argv[2])) {
  process.exit();
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    charactersUrls = JSON.parse(body).characters;
    characterNames = charactersUrls.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });

    Promise.all(characterNames)
      .then((names) => {
        names.forEach((name) => {
          console.log(name);
        });
      })
      .catch((error) => {
        console.error(error);
      });
  }
});
