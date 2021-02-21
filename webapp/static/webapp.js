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
  var gamesTable = $("#games").DataTable();
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
        gamesTable.row
          .add([
            game["name"],
            // game["sales"],
            game["publisher"],
            game["platform"],
            game["genre"],
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
      console.log(platforms.length);
      for (var k = 0; k < platforms.length; k++) {
        var platform = platforms[k];
        platformsTable.row.add([platform]).draw(false);
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
        genresTable.row.add([genre]).draw(false);
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
        publishersTable.row.add([publisher]).draw(false);
      }
    })

    .catch(function (error) {
      console.log(error);
    });
}
