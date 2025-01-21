# DICTIONARY.
SHOW SCHEMAS;
SHOW TABLES;
USE database_name;
SELECT CURRENT_USER();
CREATE DATABASE database_name;
CREATE TABLE table_name (
    column_name_1 type,
    column_name_2 type );
INSERT INTO table_name (column_1, column_2)
VALUES (value_1, value_2);


### JOURNAL.
Content input and display is one core functionality. One input box is one the page and the content entered into input box and one database is to save the entered content. Database uses MySQL and one database named sc_note is created. Currently there is only one table named Content, of which one column is for index and another is for content. Whether or not the content in the database could be operated by the application host by Express.


### OPERATION STATUS.
DATABASE
information_schema
performance_schema
mysql
sys