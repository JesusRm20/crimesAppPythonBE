CREATE TABLE table_name(
    id integer PRIMARY KEY AUTOINCREMENT,
    name char(200)
);


CREATE TABLE outcomesCount
(
    id integer PRIMARY KEY AUTOINCREMENT,
    persistent_id cahr(200)
);

CREATE TABLE outcomesCrimes
(
    id integer PRIMARY KEY AUTOINCREMENT, 
    persistent_id char(200),
    category char(200),
    date_1 char(200),
    person_id char(200)
);

CREATE TABLE streetLevelCrimes
(
    id integer PRIMARY KEY AUTOINCREMENT,
    category_id char(200) ,
    location_type char(200) ,
    latitude char(200) ,
    longitude char(200) ,
    street_id char(200) ,
    street_name char(200) ,
    context char(200) ,
    outcome_status char(200) ,
    persistent_id char(200) ,
    location_subtype char(200) ,
    month char(200)
);

CREATE TABLE users
(
    id integer PRIMARY KEY AUTOINCREMENT,
    name char(200),
    lastname char(200),
    email char(200),
    username char(200),
    password char(200),
    date char(200)
)