# Analyzing Weather in Hawaii

Conducted some climate analysis for Hawaii. 

## Step 1 - Climate Analysis and Exploration

Used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. 

### Precipitation Analysis

Retrieved 12 months of precipitation data.

* Plotted the results using the DataFrame `plot` method.

![image](https://user-images.githubusercontent.com/90559756/163404864-1d69c485-4a77-49f3-9efb-204a61212060.png)

* Used Pandas to print the summary statistics for the precipitation data.

![image](https://user-images.githubusercontent.com/90559756/163404978-765ed980-6a4f-4181-a3d1-78b8e946a938.png)


### Station Analysis

* Designed a query to calculate the total number of stations in the dataset.

* Designed a query to find the most active stations (i.e. which stations have the most rows?).

  * List the stations and observation counts in descending order.

  * Which station id has the highest number of observations?

  * Using the most active station id, calculate the lowest, highest, and average temperature.

 * Designed a query to retrieve the last 12 months of temperature observation data (TOBS).

![image](https://user-images.githubusercontent.com/90559756/163405170-e5615315-2033-4e95-84bd-241f1a9e18b4.png)

## Step 2 - Climate App

Desgiend a Flask API based on the queries conducted.

![image](https://user-images.githubusercontent.com/90559756/163406432-1b2875e4-8d3e-4dc2-bdb4-7419f5ff20d5.png)


  * Return the JSON representation of your dictionary.

  * Returned a JSON list of stations from the dataset.
  
  ![image](https://user-images.githubusercontent.com/90559756/163406138-39831515-c1fa-43f1-951d-ecff4654fbc7.png)

  * Queried the dates and temperature observations of the most active station for the last year of data.

  * Returned a JSON list of temperature observations (TOBS) for the previous year.

  * Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* Identified the average temperature in June and December at all stations across all available years in the dataset. 

* Used the Wiloxon Signed-Rank test (non-parametric paired samples t-test) to determine whether the difference in the means, if any, is statistically significant. 

![image](https://user-images.githubusercontent.com/90559756/163407449-b57ebd04-7a6d-408b-85fe-12dabe200fb9.png)


### Temperature Analysis II

* Explored weather for August first to August seventh of this year.

* Plotted the min, avg, and max temperature from this query as a bar chart.

![image](https://user-images.githubusercontent.com/90559756/163407693-2aea4009-e707-4107-90f0-3236b987c6e0.png)


### Daily Rainfall Average

* Calculated the rainfall per weather station using the previous year's matching dates.

  ![image](https://user-images.githubusercontent.com/90559756/163407769-76e51d9b-cac5-41c9-bb83-47a3704f36f5.png)

### Daily Temperature Normals

* Calculated the daily normals for the duration of the trip. Created an area plot showing the temperature minimum, average, and maximum.
![image](https://user-images.githubusercontent.com/90559756/163407942-305f2182-0daf-4940-b368-c02e65f11626.png)

