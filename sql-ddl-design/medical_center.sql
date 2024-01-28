--from the terminal run
--psql < medical_center.sql

DROP DATABASE IF EXISTS medical_center;

CREATE DATABASE medical_center;

\c medical_center

CREATE TABLE doctors 
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL
);

CREATE TABLE patients 
(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    address TEXT NOT NULL,
    phone_number VARCHAR(10) NOT NULL,
    d_o_b DATE NOT NULL,
    allergies TEXT NOT NULL
);

CREATE TABLE diseases 
(
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    icd_code VARCHAR(7) NOT NULL,
    criteria TEXT NOT NULL
);

CREATE TABLE visits 
(
    id SERIAL PRIMARY KEY,
    doctor_id INTEGER REFERENCES doctors,
    patient_id INTEGER REFERENCES patients,
    visit_date DATE NOT NULL
);

CREATE TABLE diagnoses 
(
    id SERIAL PRIMARY KEY,
    visit_id INTEGER REFERENCES visits,
    diag_id INTEGER REFERENCES diseases
);

--Tables to add:
    --Insurances
    --Departments

--Needs delete constraint

INSERT INTO doctors
    (first_name, last_name)
VALUES
    ('John', 'Smith'),
    ('Meredith', 'Grey'),
    ('John', 'Dorian');

INSERT INTO patients
    (first_name, last_name, address, phone_number, d_o_b, allergies)
VALUES  
    ('Jane', 'Doe', '123 Street Rd', '6185550123', '1994-04-10', 'cashews'),
    ('John', 'Doe', '123 Street Rd', '6185551123', '1996-11-08', 'gluten');

INSERT INTO diseases
    (name, icd_code, criteria)
VALUES
    ('COVID-19', 'F.23.15', 'dry cough, fatigue, congestion');

INSERT INTO visits
    (doctor_id, patient_id, visit_date)
VALUES 
    (1, 2, '2024-01-28'),
    (3, 1, '2024-01-26');

INSERT INTO diagnoses
    (visit_id, diag_id)
VALUES  
    (1, 1),
    (2, 1);