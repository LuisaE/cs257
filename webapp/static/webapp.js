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
  setFilters();
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
            "<a href='/publishers?name=" +
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

  var url = getAPIBaseURL() + "/genre/" + genre;

  fetch(url, { method: "get" })
    .then((response) => response.json())

    .then(function (games) {
      top_genre_games_by_sales = [];
      for (var k = 0; k < 5; k++) {
        var game = games[k];
        top_genre_games_by_sales.push(game);
      }
      var topGamesByGenre = `<h4>Top 5 ${genre} games by sales</h4>
<h4 class="small font-weight-bold">${top_genre_games_by_sales[0]["name"]} <span
  class="float-right">${top_genre_games_by_sales[0]["global_sales"]} million sales</span></h4>
<div class="progress mb-4">
<div class="progress-bar bg-danger" role="progressbar" style="width: ${top_genre_games_by_sales[0]["global_sales"]}%"
  aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<h4 class="small font-weight-bold">${top_genre_games_by_sales[1]["name"]} <span
  class="float-right">${top_genre_games_by_sales[1]["global_sales"]} million sales</span></h4>
<div class="progress mb-4">
<div class="progress-bar bg-warning" role="progressbar" style="width: ${top_genre_games_by_sales[1]["global_sales"]}%"
  aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<h4 class="small font-weight-bold">${top_genre_games_by_sales[2]["name"]} <span
  class="float-right">${top_genre_games_by_sales[2]["global_sales"]} million sales</span></h4>
<div class="progress mb-4">
<div class="progress-bar" role="progressbar" style="width: ${top_genre_games_by_sales[2]["global_sales"]}%"
  aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<h4 class="small font-weight-bold">${top_genre_games_by_sales[3]["name"]} <span
  class="float-right">${top_genre_games_by_sales[3]["global_sales"]} million sales</span></h4>
<div class="progress mb-4">
<div class="progress-bar bg-info" role="progressbar" style="width: ${top_genre_games_by_sales[3]["global_sales"]}%"
  aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<h4 class="small font-weight-bold">${top_genre_games_by_sales[4]["name"]} <span
  class="float-right">${top_genre_games_by_sales[4]["global_sales"]} million sales</span></h4>
<div class="progress">
<div class="progress-bar bg-success" role="progressbar" style="width: ${top_genre_games_by_sales[4]["global_sales"]}%"
  aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
</div><br /><p>Note: the full bar represents 100 million sales</p>`;
      if (genreDiv) {
        genreDiv.innerHTML =
          "<h2>" + genre + " Insights</h2>" + topGamesByGenre;
      }
    })

    .catch(function (error) {
      console.log(error);
    });
}

function platformInsights(platform) {
  var platformDiv = document.getElementById("platform_insight");
  var topGamesByPlatform = `<h4>Top 5 ${platform} games by sales</h4>
<h4 class="small font-weight-bold">Game 1 <span
  class="float-right">x%</span></h4>
<div class="progress mb-4">
<div class="progress-bar bg-danger" role="progressbar" style="width: 50%"
  aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<h4 class="small font-weight-bold">Game 2 <span
  class="float-right">x%</span></h4>
<div class="progress mb-4">
<div class="progress-bar bg-warning" role="progressbar" style="width: 25%"
  aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<h4 class="small font-weight-bold">Game 3 <span
  class="float-right">x%</span></h4>
<div class="progress mb-4">
<div class="progress-bar" role="progressbar" style="width: 15%"
  aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<h4 class="small font-weight-bold">Game 4 <span
  class="float-right">x%</span></h4>
<div class="progress mb-4">
<div class="progress-bar bg-info" role="progressbar" style="width: 10%"
  aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<h4 class="small font-weight-bold">Game 5 <span
  class="float-right">x%</span></h4>
<div class="progress">
<div class="progress-bar bg-success" role="progressbar" style="width: 5%"
  aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
</div>`;
  if (platformDiv) {
    platformDiv.innerHTML =
      "<h2>" + platform + " Insights</h2>" + topGamesByPlatform;
  }
}

function publisherInsights(publisher) {
  var publisherDiv = document.getElementById("publisher_insight");
  var topGamesByPublisher = `<h4>Top 5 games ${publisher} by sales</h4>
<h4 class="small font-weight-bold">Game 1 <span
  class="float-right">x%</span></h4>
<div class="progress mb-4">
<div class="progress-bar bg-danger" role="progressbar" style="width: 50%"
  aria-valuenow="20" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<h4 class="small font-weight-bold">Game 2 <span
  class="float-right">x%</span></h4>
<div class="progress mb-4">
<div class="progress-bar bg-warning" role="progressbar" style="width: 25%"
  aria-valuenow="40" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<h4 class="small font-weight-bold">Game 3 <span
  class="float-right">x%</span></h4>
<div class="progress mb-4">
<div class="progress-bar" role="progressbar" style="width: 15%"
  aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<h4 class="small font-weight-bold">Game 4 <span
  class="float-right">x%</span></h4>
<div class="progress mb-4">
<div class="progress-bar bg-info" role="progressbar" style="width: 10%"
  aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<h4 class="small font-weight-bold">Game 5 <span
  class="float-right">x%</span></h4>
<div class="progress">
<div class="progress-bar bg-success" role="progressbar" style="width: 5%"
  aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
</div>`;
  if (publisherDiv) {
    publisherDiv.innerHTML =
      "<h2>" + publisher + " Insights</h2>" + topGamesByPublisher;
  }
}

function setFilters() {
  var url = getAPIBaseURL() + "/categories/";

  fetch(url, { method: "get" })
    .then((response) => response.json())

    .then(function (categories) {
      var content = `<h3 class="small font-weight-bold">Platforms</h3>`;
      var platforms = categories["platforms"];
      for (var k = 0; k < platforms.length; k++) {
        content += `<div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" id="${platforms[k]}" value="${platforms[k]}">
        <label class="form-check-label" for="${platforms[k]}">${platforms[k]}</label>
      </div>`;
      }
      var platformsChecks = document.getElementById("platforms_checks");
      if (platformsChecks) {
        platformsChecks.innerHTML = content;
      }

      var content = `<h3 class="small font-weight-bold">Genres</h3>`;
      var genres = categories["genres"];
      for (var k = 0; k < genres.length; k++) {
        content += `<div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" id="${genres[k]}" value="${genres[k]}">
        <label class="form-check-label" for="${genres[k]}">${genres[k]}</label>
      </div>`;
      }
      var genresChecks = document.getElementById("genres_checks");
      if (genresChecks) {
        genresChecks.innerHTML = content;
      }

      var content = `<h3 class="small font-weight-bold">Publishers</h3>`;
      var publishers = categories["publishers"];
      for (var k = 0; k < publishers.length; k++) {
        content += `<div class="form-check form-check-inline">
        <input class="form-check-input" type="checkbox" id="${publishers[k]}" value="${publishers[k]}">
        <label class="form-check-label" for="${publishers[k]}">${publishers[k]}</label>
      </div>`;
      }
      var publishersChecks = document.getElementById("publishers_checks");
      if (publishersChecks) {
        publishersChecks.innerHTML = content;
      }
    })

    .catch(function (error) {
      console.log(error);
    });
}
