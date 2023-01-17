# Billboard Hot-100 Crawler

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

## 
