 DROP TABLE IF EXISTS post;
 CREATE TABLE post (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   title TEXT NOT NULL,
   'text' TEXT NOT NULL
 );