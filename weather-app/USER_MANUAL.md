# Weather App - User Manual

## Overview

The Weather App is a simple web-based application that fetches and displays current weather data for a user-selected location. It provides a visually appealing and user-friendly interface, making it easy for non-technical users to interact with and understand the information presented.

## Getting Started

To use the Weather App, simply open the `index.html` file in your preferred web browser. This will launch the app in a new browser window or tab.

![Initial App View](screenshots/initial_view.png)

## Searching for a Location

To search for a location, simply type the name of the city or town you want to view the weather data for in the search bar at the top of the app. As you type, the app will suggest possible matches for your query. You can either select a suggestion from the list or type the full name and hit the Enter key.

![Search for a Location](screenshots/search_location.png)

## Viewing Weather Data

Once you have entered a valid location, the app will fetch the current weather data from the OpenWeatherMap API and display it on the screen. The main panel will show the current temperature, weather description, and an icon representing the current weather conditions. Additional details such as humidity, wind speed, and pressure are displayed below the main panel.

![Weather Data Display](screenshots/weather_data.png)

## Updating the Weather Data

The Weather App will automatically refresh the weather data for the current location every few minutes. However, if you want to force a manual update, simply click the refresh button located next to the search bar. This will fetch the latest weather data from the API and update the display.

![Refresh Weather Data](screenshots/refresh_data.png)

## Troubleshooting

If the Weather App is unable to fetch weather data for the entered location, an error message will be displayed on the screen. This can be caused by several factors, such as an invalid location name or issues with the OpenWeatherMap API. In such cases, please verify the entered location name or try again after a few moments.

![Error Display](screenshots/error_display.png)