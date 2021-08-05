import sqlite3

#database connnection
connection=sqlite3.connect('Database_Movies.db')
cursor=connection.cursor()

#create table query
query_command=""" CREATE TABLE IF NOT EXISTS Movies(movie_name TEXT PRIMARY KEY,lead_actor TEXT,actress TEXT,year_of_release INTEGER,director_name TEXT) """
cursor.execute(query_command)

#insert into query
cursor.execute(" INSERT INTO Movies VALUES ('Pulp Fiction','Tim Roth','Amanda Plummer',1994,'Quentin Tarantino')")
cursor.execute(" INSERT INTO Movies VALUES ('The Pianist','Adrien Brody','Emilia Fox',2002,'Roman Polanski')")
cursor.execute(" INSERT INTO Movies VALUES ('Inception','Leonardo DiCaprio','Elliot Page',2010,'Christopher Nolan')")
cursor.execute(" INSERT INTO Movies VALUES ('Joker','Joaquin Phoenix','Zazie Beetz',2019,'Todd Phillips')")
cursor.execute(" INSERT INTO Movies VALUES ('Fight Club','Brad Pitt','Helena Bonham Carter',1999,'David Fincher')")


#select query
cursor.execute("SELECT * FROM Movies")
result1=cursor.fetchall()

cursor.execute("SELECT * FROM Movies WHERE lead_actor='Leonardo DiCaprio' ")
result2=cursor.fetchall()

#print the results
print(result1)
print(result2)
