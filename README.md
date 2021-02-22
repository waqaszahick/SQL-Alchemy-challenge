# SQL-Alchemy-challenge
Assignment # 9: SQL Alchemy Challenge

This is my overall 9th, second SQL, and first SQL Alchemy assignment / challenge. In "Step-1", I was required to perform "climate analysis and exploration". Also, I was required to use "Python" and "SQLAlchemy" to do basic "climate analysis" and "data exploration" of my climate database. All of the following analysis had to be completed using "SQLAlchemy ORM" queries, "Pandas", and "Matplotlib":
* Used the provided "starter" notebook and "hawaii.sqlite" files to complete my "climate analysis" and "data exploration".
* Chose a "start date" and "end date" for my trip, maaking sure that the vacation range is approximately 3-15 days total.
* Used SQLAlchemy "create_engine" to connect to my "sqlite" database.
* Used SQLAlchemy "automap_base()" to reflect my tables into classes and saved a reference to those classes called "Station" and "Measurement".

Precipitation Analysis:
* Designed a query to retrieve the last 12 months of precipitation data.
* Selected only the "date" and "prcp" (precipitation) values.
* Loadeed the query results into a "Pandas DataFrame" and set the index to the "date" column.
* Sorted the DataFrame values by "date".
* Plotted the results using the DataFrame plot method.
* Used "Pandas" to print the summary statistics for the precipitation data.

Station Analysis:
* Designed a query to calculate the total number of stations.
* Designed a query to find the most active stations, and further perforemd the following queries:
	- Listed the stations and observation counts in descending order.
	- Which station has the highest number of observations?
	- Used functions such as "func.min", "func.max", "func.avg", and "func.count" in my queries.
* Designed a query to retrieve the last 12 months of "temperature observation data" (TOBS), and performed the following:
	- Filtered by the station with the highest number of observations.
	- Plotted the results as a histogram with bins = 12.

In "Step 2" (Climate App), I designed a "Flask API" based on the afore-mentioned queries that I developed. I joined the "station" and "measurement" tables for some of the queries, used "Flask jsonify" to convert my API data into a valid "JSON" response object. Also, I used "Flask" to create the following routes:
Routes
* /
	- Home page.
	- Listed all routes that are available.
* /api/v1.0/precipitation
	- Converted the query results to a dictionary using "date" as the key and "prcp" (precipitation) as the value.
	- Returned the "JSON" representation of my dictionary.
* /api/v1.0/stations
	- Returned a "JSON" list of stations from the dataset.
* /api/v1.0/tobs
	- Queried the "dates" and "temperature observations" (TOBS) of the most active station for the last year of data.
	- Returned a "JSON" list of "temperature observations" (TOBS) for the previous year.
* /api/v1.0/<start> and /api/v1.0/<start>/<end>
	- Returned a "JSON" list of the "minimum temperature", the "average temperature", and the "max temperature" for a given "start" or "start-end" range.
	- When given the "start"  (date) only, calculated "TMIN", "TAVG", and "TMAX" for all dates greater than and equal to the "start date".
	- When given the "start" (date) and the "end date", calculated the "TMIN", "TAVG", and "TMAX" for dates between the "start" and "end date" inclusive.

As "Bonus", I perfomed the following recommended analyses:

Temperature Analysis-I:
* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?
* I was given option to either use "SQLAlchemy" or "Pandas's read_csv()" to perform this portion.
* Identifed the "average temperature" in June at all stations across all available years in the dataset, and did the same for December temperature.
* Used the "t-test" to determine whether the difference in the "means", if any, is statistically significant.
* Since "t-test" is a statistical test that is used to compare the "means" of two groups therefore, here in my assignment / challenge, I have used a paired "t-test" to compare the 'means' of first: 'average temperature' and maximum temperature', and then: 'average temperature' and minimum temperature'.

Temperature Analysis-II:
* The "starter" notebook contained a function called "calc_temps" that would accept a "start date" and "end date" in the format %Y-%m-%d. The function would return the minimum, average, and maximum temperatures for that range of dates.
* Used the "calc_temps" function to calculate the min, avg, and max temperatures for my trip using the matching dates from the previous year (i.e., use "2017-01-01" if my trip "start date" was "2018-01-01").
* Plotted the min, avg, and max temperature from my previous query as a bar chart.
	- Used the "average" temperature as the bar height.
	- Used the "peak-to-peak" (TMAX-TMIN) value as the "y error" bar (YERR).

Daily Rainfall Average:
* Calculated the rainfall per weather station using the previous year's matching dates.
* Calculated the daily normals. Normals are the averages for the min, avg, and max temperatures.
* I was provided with a function called "daily_normals" that would calculate the daily normals for a specific date. This "date" string would be in the format %m-%d. Also, I used all historic TOBS that matched that "date" string.
* Created a list of dates for my trip in the format %m-%d. Used the "daily_normals" function to calculate the normals for each date string and append the results to a list.
* Loaded the list of daily normals into a "Pandas DataFrame" and set the index equal to the date.
* Used "Pandas" to plot an area plot "(stacked = False)" for the daily normals.