import sqlalchemy

db = 'postgresql://ivoronkov:u123456@localhost:5432/ivoronkov'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


sel_1 = connection.execute("""SELECT album_name, release_year FROM album 
    WHERE release_year = 2018;
""").fetchmany(10)
print(sel_1)


sel_2 = connection.execute("""SELECT track_name, duration FROM track
    ORDER BY duration DESC;
""").fetchmany(1)
print(sel_2)


sel_3 = connection.execute("""SELECT track_name FROM track
    WHERE duration >= 210;
""").fetchmany(10)
print(sel_3)


sel_4 = connection.execute("""SELECT collection_name FROM collection
    WHERE release_year BETWEEN 2018 AND 2020;
""").fetchmany(10)
print(sel_4)


sel_5 = connection.execute("""SELECT artist_name FROM artist
    WHERE artist_name NOT LIKE '%% %%';
""").fetchmany(15)
print(sel_5)


sel_6 = connection.execute("""SELECT track_name FROM track
    WHERE track_name LIKE '%%my%%'
""").fetchmany(15)
print(sel_6)
