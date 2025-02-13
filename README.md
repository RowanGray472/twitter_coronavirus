# Coronavirus Twitter Data Analysis

This code in this repo analyzes all geotagged tweets sent in 2020 to track trends in Covid-related tweets.
The dataset in question is about 2.7TB, so I used [MapReduce](https://en.wikipedia.org/wiki/MapReduce) to parallelize the data extraction.

Specifically, I extracted the language each Tweet was sent in, what hashtags that Tweet used, and what country the Twit was from.

After consolidating the data into about 38KB in summarized JSON, I used Matplotlib to make a series of plots.
Here are the plots that analyze top countries from the whole year, by hashtag.
I only made two, but any combination is easy!

<img src=graphs/all.country%23coronavirus.png width=100% />

<img src=graphs/all.country%23코로나바이러스.png width=100% />

And here are the plots that analyzed top languages from the whole year by hashtag.

<img src=graphs/all.lang%23coronavirus.png width=100% />

<img src=graphs/all.lang%23코로나바이러스.png width=100% />

Then I got curious about the prevalence of different hashtags over time. 
So I built a separate reducer that directly converts the mapped data into a cute graph.
Here's it comparing a few hashtags.

<img src=graphs/hashtag_trend.png width=100% />
