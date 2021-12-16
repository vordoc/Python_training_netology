import sqlalchemy
import pandas as pd

db = 'postgresql://ivoronkov:u123456@localhost:5432/ivoronkov'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


# количество исполнителей в каждом жанре
sel_1 = connection.execute("""
    SELECT genre_id, COUNT(artist_id) FROM artist_genre 
    GROUP BY genre_id;
""").fetchmany(15)

print(pd.DataFrame(sel_1))
print('\n\n')


# количество треков, вошедших в альбомы 1986-1987 годов
sel_2 = connection.execute("""
    SELECT a.album_name, a.release_year, count(t.id)
    FROM album a
    JOIN track t ON a.id = t.album_id
    WHERE a.release_year >= 1986 AND a.release_year <= 1987
    GROUP BY a.album_name, a.release_year
""").fetchmany(15)

print(pd.DataFrame(sel_2))
print('\n\n')


# средняя продолжительность треков по каждому альбому
sel_3 = connection.execute("""
    SELECT  a.album_name, round(AVG(t.duration), 1)
    FROM album a
    JOIN track t ON a.id = t.album_id
    GROUP BY a.album_name
""").fetchmany(15)

print(pd.DataFrame(sel_3))
print('\n\n')


# все исполнители, которые не выпустили альбомы в 2020 году
sel_4 = connection.execute("""
    SELECT ar.artist_name, a.release_year
    FROM artist ar
    JOIN artist_album ara ON ar.id = ara.artist_id
    JOIN album a ON ara.album_id = a.id
    WHERE a.release_year != 2020
""").fetchmany(15)

print(pd.DataFrame(sel_4))
print('\n\n')


# названия сборников, в которых присутствует конкретный исполнитель (выберите сами)
sel_5 = connection.execute("""
    SELECT DISTINCT c.collection_name
    FROM collection c
    JOIN collection_track ct ON c.id = ct.collection_id
    JOIN track t ON ct.track_id = t.id
    JOIN album a ON t.album_id = a.id
    JOIN artist_album ara ON a.id = ara.album_id
    JOIN artist ar ON ara.artist_id = ar.id
    WHERE ar.artist_name LIKE 'roxette'
""").fetchmany(15)

print(pd.DataFrame(sel_5))
print('\n\n')


# название альбомов, в которых присутствуют исполнители более 1 жанра
sel_6 = connection.execute("""
    SELECT a.album_name
    FROM album a
    JOIN artist_album ara ON a.id = ara.album_id
    JOIN artist ar ON ara.artist_id = ar.id
    JOIN artist_genre ag ON a.id = ag.artist_id
    GROUP BY ar.artist_name, a.album_name
    HAVING count(ag.genre_id) > 1
""").fetchmany(15)

print(pd.DataFrame(sel_6))
print('\n\n')


# наименование треков, которые не входят в сборники
sel_7 = connection.execute("""
    SELECT t.track_name
    FROM track t
    LEFT JOIN collection_track ct ON t.id = ct.track_id
    where ct.track_id IS NULL
""").fetchmany(15)

print(pd.DataFrame(sel_7))
print('\n\n')


# исполнителя(-ей), написавшего самый короткий по продолжительности трек
# (теоретически таких треков может быть несколько)
sel_8 = connection.execute("""
    SELECT ar.artist_name, t.duration
    FROM artist ar
    JOIN artist_album ara ON ar.id = ara.artist_id
    JOIN album a ON ara.album_id = a.id
    JOIN track t ON a.id = t.album_id
    WHERE t.duration IN (SELECT MIN(duration) FROM track)
""").fetchmany(15)

print(pd.DataFrame(sel_8))
print('\n\n')


# название альбомов, содержащих наименьшее количество треков
sel_9 = connection.execute("""
    SELECT a.album_name, count(t.id)
    FROM album a
    JOIN track t  ON a.id = t.album_id
    GROUP BY a.album_name
    HAVING count(t.id) in (
        SELECT count(t.id)
        FROM album a
        JOIN track t  ON a.id = t.album_id
        GROUP BY a.album_name
        ORDER BY count(t.id)\
        LIMIT 1)
""").fetchmany(15)

print(pd.DataFrame(sel_9))
