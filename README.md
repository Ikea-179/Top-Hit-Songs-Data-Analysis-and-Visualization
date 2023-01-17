# <u>**Top Hit Songs Data Analysis & Visualization**</u>

**by Chenglin Zhang, Yijia Xue, Yushan Gu**

*names by the alphabetical order of the last names*

## Introduction

Music is an indispensable part of our life. We are born with the ability to feel and follow the rhythms, while the rhythms and melodies that lead the era also vary over time. Songs becoming top hits do not come from nowhere. They are representatives of popular culture and are even the symbol of revolution. Thus, by investigating the question of who (artists) and what (genre, audio features, etc.) is leading the ever-changing musical trend, we can get valuable insights into the development of music. Specifically, by focusing on the weekly Billboard Hot 100 since 1960, we want to illustrate the following goals: 1) the variation of genres; 2) the evolution of the top hits’ audio features; 3) who the dominant artists are on the chart; 4) what the top artists’ golden time is; 5) top artists’ musical preference (with respect to the key of songs).

## Data Preparing 

Our primary data source is Billboard Hot 100 (https://www.billboard.com/charts/hot-100/). By disabling JavaScript on the site, investigating its HTML source code, executing Python Scrapy crawler, and automatically switching the chart dates, we can retrieve the track name, artist, current week rank, last week rank, peak rank, and weeks on chart of the songs. There are 324787 records in total.

Billboard does not provide audio features and genre information. Thus, we utilized the Spotify Developer API (https://developer.spotify.com/documentation/web-api/) to retrieve the data of each track. The APIs involved include search (to match the information between the Spotify database and Billboard data), getting artist info (genre), and getting audio features (of the track). The audio features of the songs include information such as danceability, loudness, acousticness, key, mode (major or minor), valence (positiveness of the song), tempo, etc.

Then, we filtered the most popular 50 songs of each year based on their weeks on chart andqueried their audio features and artists’ genre. There are 3150 records left from 1960/01/04 to 2022/04/02, and each record has 21 variables in total. For genre, we simplified Spotify API’s response as it originally returns a detailed list of all the artist’s genres. We encoded the list of genres to a single genre from [“pop”, “rock”, “r&b”, “soul”, “hip hop/rap”, “country”] based on fuzzy matches.

## Data Crawling

***MAKE SURE to disable the JavaScript for the URL: billboard.com/charts/hot-100/ in your system's default browser before you start.***

To run the program, make sure you have the Python package **scrapy** installed in your current virtual environment.

Then, if you want to run the crawler directly, open your terminal, navigate to the **./billboard/billboard** directory where you can see several scrapy initialization and setting files. Run the following command 

```shell
scrapy crawl hot100 -o hot100.csv
```

in your terminal. Normally, it would take about 1 hour to crawl the data from 2022-04-02 to 1960. Then, you can see an output CSV file in your current working directory.

To test the **scrapy** CLI, run the following command in your terminal:

```shell
scrapy shell billboard.com/charts/hot-100/
```

Then, an interactive shell will start, in which you can test the scrapy commands that you want.

The main function of this scraper can be found at **./billboard/billboard/spider/hot100.py**.

## **Results**

The interactible visualization link for this project: https://public.tableau.com/app/profile/yijia.xue/viz/STATS401Project1/Dashboard1

![Visualization](Visualization.png)
