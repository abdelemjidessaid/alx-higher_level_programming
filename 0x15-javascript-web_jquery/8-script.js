$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const results = data.results;
  results.forEach(movie => {
    $('ul#list_movies').append('<li>' + movie.title + '</li>');
  });
});
