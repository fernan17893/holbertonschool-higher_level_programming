$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  for (let i = 0; i < data.results.length; i++){
      $(`<li>${data.results[i].title}</li>`).appendTo('#list_movies')
  };
});
