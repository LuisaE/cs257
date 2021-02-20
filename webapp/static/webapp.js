// Claire Williams and Luisa Escosteguy

window.onload = initialize;

function initialize() {
  gamesTable = initialize_data_tables();
  getGames(gamesTable);
}

function initialize_data_tables() {
  var gamesTable = $("#games").DataTable();
  $("#platforms").DataTable();
  $("#publishers").DataTable();
  $("#genres").DataTable();
  return gamesTable;
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
            game["birth_year"],
            game["death_year"],
            game["description"],
          ])
          .draw(false);
      }
    })

    .catch(function (error) {
      console.log(error);
    });
}
