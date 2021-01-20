# Develop and deploy a data dashboard

Web dashboard to visualize data gathered from the world bank website. Data wrangling is done using pandas and then visualised using Plotly. The web app is hosted on Heroku.

The dashboard shows economic indicators for BRICs (group of 5 important emerging countries around the world) and USA.

## Table of contents
1. [Installation](#Installation)
2. [Project Motivation](#Project-Motivation)
3. [File Descriptions](#File-Descriptions)
4. [Results](#Results)
5. [Licensing, Authors, Acknowledgements](#Licensing-Authors-Acknowledgements)

## Installation

The code should run with no issues using Python versions 3.*. Python packages needed are in the requirement file.

## Project Motivation

The goal of this project is to create a data dashboard using Bootstrap, Plotly, Flask and then deploy it as an application on cloud with Heroku. That done, we will be able to visualize data online and interactively.

  
## File Descriptions

The app uses data stored in the data/ folder.

The data is cleaned and prepared for plotting in wrangle_data.py file.

The html template is found in index.html, including divs for the plots.

The file routes.py imports the prepared figures from wrangle_data.py to plot them inside the index.html.

This is the [link of world bank website](https://www.worldbank.org/) where you can find the csv files.

## Results

The result of this project can be found in this [web address.](https://thiagogaviolidashboard.herokuapp.com/)

## Licensing, Authors, Acknowledgements

Must give credit to World Bank for the data. The code can be used as any person demands.
