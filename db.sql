DROP DATABASE IF EXISTS cinema;
CREATE DATABASE cinema;
USE cinema;


CREATE TABLE User 
(
	username NVARCHAR(30) NOT NULL,
	password NVARCHAR(20) NOT NULL,
	name NVARCHAR(25) NOT NULL,
	last_name NVARCHAR(25) NOT NULL,
	email NVARCHAR(25) NOT NULL,
	primary key (username)

);

CREATE TABLE Sala
(
	sala_id INT AUTO_INCREMENT NOT NULL,
	sala_number INT NOT NULL,
	number_of_seats INT NOT NULL,
	primary key (sala_id)

);

CREATE TABLE Movie
(
	movie_id INT AUTO_INCREMENT NOT NULL,
	title NVARCHAR(20) NOT NULL,
	descr NVARCHAR(30) NOT NULL,
	duration INT NOT NULL,
	primary key (movie_id)

);

CREATE TABLE Schedule
(
	schedule_id INT NOT NULL AUTO_INCREMENT,
	movie_id INT REFERENCES Movie(movie_id),
	sala_id INT REFERENCES Sala(sala_id),
	datentime DATETIME NOT NULL,
	available_seats INT NOT NULL,
	primary key (schedule_id)

);

CREATE TABLE Ticket
(
	ticket_id INT NOT NULL AUTO_INCREMENT,
	username NVARCHAR(20) REFERENCES User(username),
	schedule_id INT NOT NULL REFERENCES Schedule(schedule_id),
	seat_number INT NOT NULL,
	primary key (ticket_id)

);


INSERT INTO Movie VALUES (1, "Movie 1", "Just a little short movie", 120);
INSERT INTO Movie VALUES (2, "Movie 2", "Another short movie", 160);
INSERT INTO Movie VALUES (3, "Movie 3", "Last one, long movie", 180);
INSERT INTO Sala VALUES (1, 1, 90);
INSERT INTO Sala VALUES (2, 2, 90);
INSERT INTO Sala VALUES (3, 3, 80);


INSERT INTO Schedule VALUES (1, 1, 1, "2019-12-01 08:00:00", 90);
INSERT INTO Schedule VALUES (2, 1, 1, "2019-12-01 09:45:00", 90);
INSERT INTO Schedule VALUES (3, 1, 1, "2019-12-01 11:30:00", 90);
INSERT INTO Schedule VALUES (4, 1, 1, "2019-12-01 13:15:00", 90);
INSERT INTO Schedule VALUES (5, 2, 2, "2019-12-01 08:00:00", 90);
INSERT INTO Schedule VALUES (6, 2, 2, "2019-12-01 09:45:00", 90);
INSERT INTO Schedule VALUES (7, 2, 2, "2019-12-01 11:30:00", 90);
INSERT INTO Schedule VALUES (8, 2, 2, "2019-12-01 13:15:00", 90);
INSERT INTO Schedule VALUES (9, 3, 3, "2019-12-01 09:15:00", 80);
INSERT INTO Schedule VALUES (10, 3, 3, "2019-12-01 11:15:00", 80);
INSERT INTO Schedule VALUES (11, 3, 3, "2019-12-01 12:30:00", 80);
INSERT INTO Schedule VALUES (12, 1, 1, "2019-12-02 08:00:00", 90);
INSERT INTO Schedule VALUES (13, 1, 1, "2019-12-02 09:45:00", 90);
INSERT INTO Schedule VALUES (14, 1, 1, "2019-12-02 11:30:00", 90);
INSERT INTO Schedule VALUES (15, 1, 1, "2019-12-02 13:15:00", 90);



INSERT INTO User VALUES ("emmanuelgallardomago", "123", "Emmanuel", "Gallardo", "deg4_gow@hotmail.com");
INSERT INTO User VALUES ("pedrochido", "1234", "Pedro", "Garcia", "pedroeschido@gmail.com");

INSERT INTO Ticket VALUES(1, "emmanuelgallardomago", 1, 1);
INSERT INTO Ticket VALUES(2, "emmanuelgallardomago", 1, 20);
INSERT INTO Ticket VALUES(3, "emmanuelgallardomago", 1, 30);

CREATE VIEW Movies
AS 
SELECT sch.schedule_id, m.title, m.duration, sch.datentime, sa.sala_number
FROM Movie m, Schedule sch, Sala sa
WHERE m.movie_id = sch.movie_id
AND sch.sala_id = sa.sala_id
ORDER BY sch.datentime;

CREATE VIEW Schedule_View
AS
SELECT sch.schedule_id, m.title, m.movie_id 
FROM Schedule sch, Movie m, Sala sa
WHERE m.movie_id = sch.movie_id
AND sch.sala_id = sa.sala_id


