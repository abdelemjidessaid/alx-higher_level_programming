-- Script that creates the database hbtn_0d_2 and the user user_0d_2.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT PRIVILEGES SELECT TO 'user_0d_2'@'localhost' ON hbtn_0d_2.*;