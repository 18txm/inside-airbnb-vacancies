# Forecasting Airbnb Vacancy: Unveiling the Impact of Location Dynamics and Booking Requirements
This projects seeks to explore the ability to predict vacancy rates in London Airbnbs. Throughout this repository, three research questions are explored,
checking if different sets of attributes are able to predict vacancy rates, whether short term or long term.

## Description
Airbnb is an online marketplace for short-term rentals of apartments, homes, and vacation properties. The website
allows hosts to list their properties, along with information including the number of bedrooms, bathrooms, and the
price per night. In large metropolitan areas, hosts can struggle to complete with tens of thousands of other
property listings for renters. To maximize profitability, hosts must be able to minimize the number of days that their
properties remains vacant. This report analyzes the various factors which can contribute to Airbnb property vacancy in large cities.

There are many reasons behind this study. Understanding potential vacancies in properties can help customers plan their trips better.
Additionally, understanding which properties are in high-demand could help rental agencies and property managers distribute their resources better.
All in all, predicting a city's airbnb vacancy market is a powerful tool with many potential benefits.

## Table of Contents
- Installation
- Usage
- Installation

## Usage
This project is used to estimate vacancy rates based on the Inside Airbnb dataset. There are three research questions:
- RQ1: Estimating Vacancy Rates based on reviews from customers.
- RQ2: Estimating Vacancy Rates based on booking requirements.
- RQ3: Estimating Vacancy Rates based on Geographical Position of the listing.
Each research question, EDA, and prediction model is featured in their respective Jupyter Notebook.

The main methodology is implemented in "rq1.ipynb", "rq2.ipynb", and "rq3.ipynb".
Additionally, preliminary EDA is achieved in "EDA" folder for both the listing.csv dataset and the calendar.csv dataset.

## Dataset
The dataset being used is the "Inside Airbnb" dataset, which provides the general public with a summary of Airbnb statistics for different cities.

## Installation
Here are a list of requirements:
- Pandas
- Numpy
- Seaborn
- sci-kit learn
- os
- matplotlib
- Python 3.11 (RQ2 is run on Python 3.10.12)
- Keras
