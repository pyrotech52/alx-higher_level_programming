$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  $.each(data.results, (key, value) => {
    $('UL#list_movies').append(`<li>${value.title}</li>`);
  });
});