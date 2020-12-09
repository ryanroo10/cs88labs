.read data.sql

-- Q2
CREATE TABLE obedience as
  -- REPLACE THIS LINE
  SELECT seven, gerald FROM students;


-- Q3
CREATE TABLE blue_dog as
  -- REPLACE THIS LINE
  SELECT color, pet FROM students WHERE color = 'blue' AND pet = 'dog';


-- Q4
CREATE TABLE smallest_int as
  -- REPLACE THIS LINE
  SELECT time, smallest FROM students WHERE smallest > 3 ORDER BY smallest ASC LIMIT 20;


-- Q5
CREATE TABLE sevens as
  -- REPLACE THIS LINE
  SELECT a.seven FROM students as a, checkboxes as b
    WHERE a.time = b.time AND a.number = 7 AND b."7" = "True";


-- Q6
CREATE TABLE matchmaker as
  -- REPLACE THIS LINE
  SELECT a.pet, a.song, a.color, b.color FROM students AS a, students AS b
    WHERE a.time < b.time AND a.pet = b.pet AND a.song = b.song;


-- Q7
CREATE TABLE smallest_int_count as
  -- REPLACE THIS LINE
  SELECT smallest, count(*) from students where smallest >= 1
    group by smallest;
