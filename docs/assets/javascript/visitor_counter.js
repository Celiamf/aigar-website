(function () {
  const countApiUrl = "https://api.countapi.xyz/hit";
  const url = countApiUrl + window.location.pathname;

  console.log(countApiUrl, window.location.pathname, url);

  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("page-views").textContent = data.value;
    })
    .catch((error) => console.error("Error al obtener las visitas:", error));
})();
