--from the terminal run
--psql < soccer_league.sql

DROP DATABASE IF EXISTS soccer_league;

CREATE DATABASE soccer_league;

\c soccer_league

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(15) NOT NULL,
    coach TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    number INTEGER NOT NULL,
    position VARCHAR(6),
    team_id INTEGER REFERENCES teams
);

CREATE TABLE referees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL
);

CREATE TABLE seasons (
    id SERIAL PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(15) NOT NULL,
    address TEXT NOT NULL
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    home_team INTEGER REFERENCES teams,
    away_team INTEGER REFERENCES teams,
    location_id INTEGER REFERENCES locations,
    date DATE NOT NULL,
    time INTEGER NOT NULL,
    winner INTEGER REFERENCES teams,
    season_id INTEGER REFERENCES seasons,
    ref_id INTEGER REFERENCES referees
);

CREATE TABLE goals (
    id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players,
    matches_id INTEGER REFERENCES matches
);

CREATE TABLE roster (
    id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players,
    team_id INTEGER REFERENCES teams,
    matches_id INTEGER REFERENCES matches
);

--Could add tables:
    --Rankings?