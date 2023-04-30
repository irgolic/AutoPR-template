// script.js

const apiKey = "YOUR_API_KEY";
const weatherApiUrl = "https://api.openweathermap.org/data/2.5/weather";

const searchInput = document.querySelector("#search-input");
const searchButton = document.querySelector("#search-button");

const locationName = document.querySelector("#location-name");
const temperature = document.querySelector("#temperature");
const weatherDescription = document.querySelector("#weather-description");
const weatherIcon = document.querySelector("#weather-icon");

function displayWeatherData(data) {
  locationName.textContent = `${data.name}, ${data.sys.country}`;
  temperature.textContent = `${Math.round(data.main.temp)}°C`;
  weatherDescription.textContent = data.weather[0].description;
  weatherIcon.src = `http://openweathermap.org/img/w/${data.weather[0].icon}.png`;
}

function fetchWeatherData(location) {
  fetch(`${weatherApiUrl}?q=${location}&units=metric&appid=${apiKey}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch weather data");
      }
      return response.json();
    })
    .then((data) => {
      displayWeatherData(data);
    })
    .catch((error) => {
      console.error("Error fetching weather data:", error);
    });
}

searchButton.addEventListener("click", () => {
  fetchWeatherData(searchInput.value);
});