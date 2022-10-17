# Python-US-Bikeshare-Data
In this project I used Python to explore data related to bike share systems for three major cities in the United States.


<h2>Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.</h2>

Tables are designed to optimize queries on song play analysis. With this database Sparkify can query for example the location, time or gender of their user. The app's user behaveior becomes more improtant when Sparkify checks for the conversion rates and the portential gorwth of the startup.


<h2>How to run the Python scripts</h2>

1. execute "python create_tables.py"
2. then "python etl.py"

<h2>An explanation of the files in the repository</h2>

create_tables.py creates or if necessary drops tables from the dataset

etl.ipynb python jupyter notebook for testing the ETL process with one song file

etl.py actual ETL python script which extracts, transfroms and loads the data into the database

sql_querries.py SQL querries whcih will be imported into the etl.py file

test.ipynb python jupyter notebook used to see if data was succesfully loaded to a table

<h2>State and justify your database schema design and ETL pipeline.</h2>

For this database we chose a star schema because it is more effective for simple querries.
The Fact Table contains all entries/info that relate to the played song
