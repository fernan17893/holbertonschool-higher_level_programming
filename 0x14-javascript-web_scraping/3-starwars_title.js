#!/usr/bin/node
/* Script prints title of SW movie with match episode */

const axios = require('axios');

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])

  .then(response => {
    console.log(response.data.title);
  })
  .catch(error => {
    console.log(error.status);
  });
