create database station;
use station;
CREATE TABLE Station(
	id INT PRIMARY KEY,
    city VARCHAR(20),
    state VARCHAR(2), 
	latitude_North real,
    longitude_west real
    );
 
 Insert Into Station Values (13,"Phoenix", "AZ", "33", "112");
 Insert Into Station Values (44, "Denver", "CO", "40", "105");
 Insert Into Station values (66, "Caribou", "ME", "47", "68");

SELECT * FROM STATION ;

SELECT * FROM STATION
where latitude_North > 39.5;

CREATE TABLE STATS
(ID INTEGER REFERENCES STATION(ID),
 MONTH INTEGER CHECK (MONTH BETWEEN 1 AND 12),
 TEMP_F REAL CHECK (TEMP_F BETWEEN -80 AND 150),
 RAIN_I REAL CHECK ( RAIN_I BETWEEN 0 AND 100),
 PRIMARY KEY (ID, MONTH));

Insert into stats values (13, "1", "57.4",".31");
Insert into stats values (13, "7", "91.7","5.15");
Insert into stats values (44, "1", "27.3", ".18");
Insert into stats values (44, "7", "74.8", "2.11");
Insert into stats values (66, "1", "6.7", "2.1");
Insert into stats values (66, "7", "65.8", "4.52");

SELECT * FROM STATS;

SELECT * FROM STATION, STATS
WHERE STATION.ID = STATS.ID;

SELECT MONTH, TEMP_F, RAIN_I
FROM STATS
ORDER BY MONTH, RAIN_I DESC;

SELECT latitude_North, CITY, TEMP_F
FROM STATS, STATION 
WHERE MONTH = 7
AND STATS.ID = STATION.ID
ORDER BY TEMP_F;

SELECT MAX(TEMP_F), MIN(TEMP_F), AVG(RAIN_I)
FROM STATS
GROUP BY ID;

UPDATE STATS SET RAIN_I = RAIN_I+0.01;
SELECT * FROM STATS

UPDATE STATS SET TEMP_F = 74.9
WHERE ID =44
AND MONTH = 7;

