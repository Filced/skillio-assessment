CREATE DATABASE assessment;

CREATE TABLE IF NOT EXISTS flights 
(id SERIAL PRIMARY KEY,
flight_number VARCHAR(10),
departure_time TIMESTAMP,
arrival_time TIMESTAMP,
departure_airport VARCHAR(50),
destination_airport VARCHAR(50));

INSERT INTO 
flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport)
VALUES
('SK1742', '2025-06-19 16:30:00', '2025-06-20 08:15:00', 'Arlanda Airport', 'Melbourne Airport'),
('TK1974', '2025-07-03 19:30:00', '2025-07-03 21:00:00', 'Copenhagen Airport', 'Berlin Airport'),
('SJ25L1', '2026-01-05 05:45:00', '2026-01-06 10:30:00', 'Amsterdam Airport', 'Cypress Airport');


--  V  BONUS SQL TASK  V

CREATE TABLE IF NOT EXISTS airlines
(id SERIAL PRIMARY KEY,
name VARCHAR(50),
flights_id INT,
CONSTRAINT fk_flight_id
    FOREIGN KEY (flights_id)
        REFERENCES flights(id)
    ON DELETE CASCADE 
);

INSERT INTO 
airlines (name, flights_id)
VALUES
('SAS', 1),
('Ving', 2),
('SAS', 6),
('Norwegian', 3),
('Ryanair', 8),
('Scandinavian Airlines', 7);