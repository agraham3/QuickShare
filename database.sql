DROP DATABASE IF EXISTS quickShare;
CREATE DATABASE quickShare;
USE quickShare;
CREATE TABLE User
(
ID int NOT NULL AUTO_INCREMENT,
username varchar(15) NOT NULL,
password varchar(25) NOT NULL,
PRIMARY KEY (ID)
);
CREATE TABLE Album
(
ID int NOT NULL AUTO_INCREMENT,
user_id int,
name varchar(40) NOT NULL,
PRIMARY KEY (ID)
);
CREATE TABLE Image
(
ID int NOT NULL AUTO_INCREMENT,
user_id int,
name varchar(40) NOT NULL,
PRIMARY KEY (ID)
);
