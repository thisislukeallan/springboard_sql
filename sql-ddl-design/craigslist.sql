--from the terminal run
--psql < craigslist.sql

DROP DATABASE IF EXISTS craigslist;

CREATE DATABASE craigslist;

\c craigslist

CREATE TABLE regions 
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE users 
(
    id SERIAL PRIMARY KEY,
    username VARCHAR(10) NOT NULL,
    password VARCHAR(15) NOT NULL,
    region_id INTEGER REFERENCES regions
);

CREATE TABLE categories 
(
    id SERIAL PRIMARY Key,
    name VARCHAR(15) NOT NULL
);

CREATE TABLE posts 
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    price INTEGER,
    content TEXT NOT NULL,
    location TEXT NOT NULL,
    user_id INTEGER REFERENCES users,
    region_id INTEGER REFERENCES regions,
    category_id INTEGER REFERENCES categories 
);

INSERT INTO regions
    (name)
VALUES
    ('San Francisco'),
    ('Atlanta'),
    ('Seattle'),
    ('St.Louis');

INSERT INTO users
    (username, password, region_id)
VALUES
    ('user1', 'password', 1),
    ('user2', 'pa$$word', 3),
    ('user3', 'drowssap', 2);

INSERT INTO categories
    (name)
VALUES
    ('Housing'),
    ('Vehicles'),
    ('Toys');

INSERT INTO posts
    (title, price, content, location, user_id, region_id, category_id)
VALUES
    ('2014 Toyota Corolla', 2300, 'Great car, runs good, need gone', '22 miles', 1, 2, 2),
    ('Ninja Turtle Toys Antique', 1500, 'Mint condition, collector set', '14 miles', 3, 4, 3),
    ('Home for rent', 750, '1 bed, 1 bath, great location', '35 miles', 2, 2, 1);

