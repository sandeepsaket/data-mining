Please read this before executing the project:-

---------
Plugins-
---------
Software: python3(.sh files run python3 files)


--------------
Dependencies-
--------------
Python Libraries: pandas, numpy, matplotlib, seaborn, datetime

For installation of this modules:

In bash terminal type:  pip install numpy
In bash terminal type:  pip install pandas
In bash terminal type:  pip install matplotlib
In bash terminal type:  pip install seaborn


--------------
Datasets-
--------------
All the datasets used for the project are provided in the same folder. 
List of datasets is as follows:
1. boxoffice.csv
2. boxoffice_actors.csv
3. BollywoodDirectorRanking.csv
4. BollywoodActorRanking.csv
5. Data for repository.csv
6. indian movies.csv
7. bollywood_full_1950-2019.csv
8. bollywood_crew_1950-2019.csv
9. bollywood_crew_data_1950-2019.csv
10. bollywood_box_clean.csv
11. bollywood_movies.csv


----------------
Data Collection- 
----------------
Few of the datasets have been scraped from the websites and code for that has also been provided.


-----------
Programs-
-----------
.sh files:

project.sh 
  Top level script that runs the entire project


movie-revenue-ranking.sh
  Runs dm1.py python file

  Generates movie-ranking-gross-collection.csv, movie-ranking-profit-made.csv, movie-ranking-profit-percent.csv

  These output files rank the movies based on their gross collection, profit made and profit percent.


genre-collection-rating.sh
  Runs dm2.py python file
  
  Generates  genre-collection.csv, rating-collection.csv, genre-collection-graph.png, rating-collection-graph.png
  
  These output files show the comparision of revenue collected by movies with different genres and ratings. 


year-genre-collection.sh
  Runs dm3.py python file

  Generates most-used-genre.csv, year-collection.csv, year-collection-graph.png

  These output files show the 5 most used genres for past year (1950-2020) and also compare the average collection of movies over the years.


language-movie.sh
  Runs dm4.py python file

  Generates language-movies.csv

  This output file shows the number of movies released for different languages in India and also best and average rating for these movies.


popular-actor-director.sh
  Runs dm5.py python file
  
  Generates maximum-movies-actor.csv, maximum-movies-actor-graph.png, maximum-movies-director.csv, maximum-movies-director-graph.png, popular-actor.csv, popular-actor-graph.png,
  popular-director.csv, popular-director-graph.png
  
  These output files show the top ten actors and directors that are most popular and top ten that have maximum number of movies and also compares their ratings.


genre-ranking.sh
  Runs dm6.py python file
  
  Generates genre-ranking-average-gross.csv, genre-ranking-average-profit.csv, genre-ranking-popular.csv, genre-ranking-total-gross.csv, genre-ranking-total-profit.csv,
  screen-gross-graph.png
  
  These output files rank the genres and movies based on gross collection, profit and popularity. The graph shows the significance of screen count on profit.


actor-director-movie.sh
  Runs dm7.py python file

  Generates actor-movierating.csv, director-movierating.csv

  These output files rank the actor and director based on imdb rating of their movies.


actor-director-genre.sh
  Runs dm8.py python file

  Generates actor-genre.csv, director-genre.csv

  These output files show the genre in which the actor and the director have worked the most.


collection-india-worldwide.sh
  Runs dm9.py python file

  Generates collection-india-worldwide.csv

  This output file compares collection of movies in India and worldwide. Also this file show the percentage of revenue collected on the opening day and on first weekend  


most-successful.sh
  Runs dm10.py python file

  Generates net-mostsuccessful.csv, worldwide-mostsuccessful.csv

  These output files show the most successful bollywood actor, producer, banner and director worldwide and in India. 


movie-ranking.sh
  Runs dm11.py python file

  Generates movie-score.csv

  This output file ranks the movies based on imdb rating and revenue made.


crew-ranking.sh
  Runs dm12.py pyhton file

  Generates acotr-score.csv, director-score.csv

  This output files ranks the actors and directors based on imdb rating and revenue made.


revenue-budget-ratio.sh
  Runs dm13.py python file

  Generates actor-type-revenue-budget-ratio-graph.png, release-day-revenue-budget-ratio-graph.png

  These output files show the comparision of revenue to budget ratio for movies having a rookie actor and veteran actor. Also for a normal release day and a holiday release.


month-collection.sh
  Runs dm14.py python file

  Generates month-footfalls.csv, month-total-collection.csv

  These output files show the best month for past year where maximum amount of collection was done.


yearwise-highest.sh
  Runs dm15.py pyhton file

  Generates yearwise-highest-actor.csv, yearwise-highest-movies.csv

  These output files show the best actors and movies depending on yearly collection(India and overseas) and footfalls.

top20-collection.sh
  Runs dm16.py pyhton file

  Generates top20-actor-highestcoll.csv, top20-director-highestcoll.csv, top20-producer-highestcoll.csv

  These output files show the top 20 actors, directors and producers whose movies(all movies combined) have made maximum revenue.

debut-movie-year.sh
  Runs dm17.py pyhton file

  Generates actors-debut.csv, directors-debut.csv, producer-debut.csv

  These output files show for each actor, director and producer their debut movie and year.

verdict.sh
  Runs dm18.py pyhton file

  Generates actors-movies-verdict.csv, directors-movies-verdict.csv, producers-movies-verdict.csv

  These output files show the actor, director and producer which has most movies in categories going from all time blockbuster to disaster.

best-teams.sh
  Runs dm19.py pyhton file

  Generates actor-director-highestgross.csv, producer-actor-highestgross.csv, producer-director-highestgross.csv

  These output files give the top 20 teams of actor-director, producer-actor and producer-director that have the highest all time collection on the boxoffice

footfalls.sh
  Runs dm20.py pyhton file

  Generates moives-club.csv, topactors-footfalls.csv, topdirectors-footfalls.csv, topproducers-footfalls.csv

  These output files give the number of movies in the 300, 200 and 100 crore club and also the top actor, director and producer based on the total number of movies they have in these clubs.
  It also ranks the actors, directors and producers on the number of tickets sold for their movies.


-----------
How to use:
-----------
To run the whole project at once open tha terminal at location of analysis system and run the following command on terminal-
bash project.sh 

To run each code seperately run the following command from the terminal-
bash FILE_NAME.sh
where FILE_NAME is the name of the .sh file you want to run


--------
Output-
--------
All the output files generated are stored in the 'output-files' folder.

Output files are better elaborated in the report.


-----------------------------
Some points to keep in mind:
-----------------------------
If any sh file does not execute please change permissions for the file and try again.

All the python programs and the datasets are provided in the same folder. Python program are named dm1, dm2, dm3, and so on.
   
Please keep all the python programs, the datasets and the output-files folder within the same directory otherwise, there will be execution errors.

  