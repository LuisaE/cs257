// Claire Williams and Luisa Escosteguy

window.onload = initialize;

function initialize() {
  [
    gamesTable,
    platformsTable,
    publishersTable,
    genresTable,
  ] = initialize_data_tables();
  getGames(gamesTable);
  getPlatforms(platformsTable);
  getGenres(genresTable);
  getPublishers(publishersTable);
}

function initialize_data_tables() {
  var gamesTable = $("#games").DataTable({
    order: [[1, "desc"]],
  });
  var platformsTable = $("#platforms").DataTable();
  var publishersTable = $("#publishers").DataTable();
  var genresTable = $("#genres").DataTable();
  return [gamesTable, platformsTable, publishersTable, genresTable];
}

function getAPIBaseURL() {
  var baseURL =
    window.location.protocol +
    "//" +
    window.location.hostname +
    ":" +
    window.location.port +
    "/api";
  return baseURL;
}

function getGames(gamesTable) {
  var url = getAPIBaseURL() + "/games/";

  fetch(url, { method: "get" })
    .then((response) => response.json())

    .then(function (games) {
      for (var k = 0; k < games.length; k++) {
        var game = games[k];
        //for now with links are plural just to test - inshights should be singular
        gamesTable.row
          .add([
            game["name"],
            game["sales"],
            "<a href='/publishers" +
              game["publisher"] +
              "'>" +
              game["publisher"] +
              "</a>",
            "<a href='/platforms?name=" +
              game["platform"] +
              "'>" +
              game["platform"] +
              "</a>",
            "<a href='/genres?name=" +
              game["genre"] +
              "'>" +
              game["genre"] +
              "</a>",
            game["year"],
          ])
          .draw(false);
      }
    })

    .catch(function (error) {
      console.log(error);
    });
}

function getPlatforms(platformsTable) {
  var url = getAPIBaseURL() + "/platforms/";

  fetch(url, { method: "get" })
    .then((response) => response.json())

    .then(function (platforms) {
      for (var k = 0; k < platforms.length; k++) {
        var platform = platforms[k];
        platformsTable.row
          .add([
            `<a href='#' onclick='platformInsights("${platform}")'>` +
              platform +
              "</a>",
          ])
          .draw(false);
      }
    })

    .catch(function (error) {
      console.log(error);
    });
}

function getGenres(genresTable) {
  var url = getAPIBaseURL() + "/genres/";

  fetch(url, { method: "get" })
    .then((response) => response.json())

    .then(function (genres) {
      for (var k = 0; k < genres.length; k++) {
        var genre = genres[k];
        genresTable.row
          .add([
            `<a href='#' onclick='genreInsights("${genre}")'>` + genre + "</a>",
          ])
          .draw(false);
      }
    })

    .catch(function (error) {
      console.log(error);
    });
}

function getPublishers(publishersTable) {
  var url = getAPIBaseURL() + "/publishers/";

  fetch(url, { method: "get" })
    .then((response) => response.json())

    .then(function (publishers) {
      for (var k = 0; k < publishers.length; k++) {
        var publisher = publishers[k];
        publishersTable.row
          .add([
            `<a href='#' onclick='publisherInsights("${publisher}")'>` +
              publisher +
              "</a>",
          ])
          .draw(false);
      }
    })

    .catch(function (error) {
      console.log(error);
    });
}

function genreInsights(genre) {
  var genreDiv = document.getElementById("genre_insight");
  if (genreDiv) {
    genreDiv.innerHTML =
      "<h2>" +
      genre +
      " Insights</h2> <p>Content will show up here when the feature is ready</p>";
  }
}

function platformInsights(platform) {
  var platformDiv = document.getElementById("platform_insight");
  if (platformDiv) {
    platformDiv.innerHTML =
      "<h2>" +
      platform +
      " Insights</h2> <p>Content will show up here when the feature is ready</p>";
  }
}

function publisherInsights(publisher) {
  var publisherDiv = document.getElementById("publisher_insight");
  if (publisherDiv) {
    publisherDiv.innerHTML =
      "<h2>" +
      publisher +
      " Insights</h2> <p>Content will show up here when the feature is ready</p>";
  }
}
