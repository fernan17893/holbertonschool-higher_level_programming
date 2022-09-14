#!/usr/bin/node
/* display the status of a GET request */

const axios = require('axios');

axios.get(process.argv[2])
  .then(resp => {
    console.log('code: ', resp.status);
  })
  .catch(error => {
    if (error.response)
    console.log('code: ', error.response.status);
  });
