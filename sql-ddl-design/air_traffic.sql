-- from the terminal run:
-- psql < air_traffic.sql

DROP DATABASE IF EXISTS air_traffic;

CREATE DATABASE air_traffic;

\c air_traffic

CREATE TABLE seats
(
  seat_id VARCHAR(4) PRIMARY KEY
);

CREATE TABLE airlines
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE cities
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE countries
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE tickets
(
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  seat_id VARCHAR REFERENCES seats(seat_id),
  departure TIMESTAMP NOT NULL,
  arrival TIMESTAMP NOT NULL,

  airline_id INTEGER REFERENCES airlines,
  from_city_id INTEGER REFERENCES cities,
  from_country_id INTEGER REFERENCES countries,
  to_city_id INTEGER REFERENCES cities,
  to_country_id INTEGER REFERENCES countries
);