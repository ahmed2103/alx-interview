#!/usr/bin/node
/*
get Star Wars characters from the Star Wars API
 */

const request = require('request');
const process = require('process');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    JSON.parse(body).characters.forEach(url => {
      request(url, (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
