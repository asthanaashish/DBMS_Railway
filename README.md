# DBMS_Railway
undergoing Project


try by first install all requirement packages from requirement.txt file

open venv folder of the whole project and clone the repo there


in database
 create test2 database
 in that db create tables
 +-----------------+
| Tables_in_test2 |
+-----------------+
| canc            |
| station         |
| train           |
| username        |
| users           |
+-----------------
keep desc of each table as following

mysql> desc users;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| fname   | varchar(30) | YES  |     | NULL    |       |
| last    | varchar(30) | YES  |     | NULL    |       |
| email   | varchar(40) | NO   | PRI | NULL    |       |
| city    | varchar(20) | YES  |     | NULL    |       |
| pincode | varchar(20) | YES  |     | NULL    |       |
| dob     | varchar(20) | YES  |     | NULL    |       |
| gender  | varchar(5)  | YES  |     | NULL    |       |
| address | varchar(40) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+


mysql> desc username;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| username | varchar(10) | NO   |     | NULL    |       |
| password | varchar(10) | YES  |     | NULL    |       |
| email    | varchar(40) | NO   | PRI | NULL    |       |
+----------+-------------+------+-----+---------+-------+





mysql> desc train;
+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| train_no       | int         | YES  |     | NULL    |       |
| train_name     | varchar(20) | YES  |     | NULL    |       |
| source_station | varchar(20) | YES  |     | NULL    |       |
| destination    | varchar(20) | YES  |     | NULL    |       |
| scheduled_day  | varchar(20) | YES  |     | NULL    |       |
+----------------+-------------+------+-----+---------+-------+







mysql> desc station;
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | int         | NO   | MUL | NULL    | auto_increment |
| sname | varchar(50) | NO   | PRI | NULL    |                |
+-------+-------------+------+-----+---------+----------------+





mysql> desc canc;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| pnr   | varchar(20) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+





