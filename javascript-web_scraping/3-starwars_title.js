#!/usr/bin/node
const movieID = process.argv[2];
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
