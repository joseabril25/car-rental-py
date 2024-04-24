-- schema.sql

-- Create the Users table
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

-- Create the Cars table
CREATE TABLE IF NOT EXISTS Cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER NOT NULL,
    mileage INTEGER,
    available_now INTEGER NOT NULL,
    min_rent_period INTEGER NOT NULL,
    max_rent_period INTEGER NOT NULL
);

-- Create the Rentals table
CREATE TABLE IF NOT EXISTS Rentals (
    rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status TEXT NOT NULL, -- such as 'pending', 'approved', 'rejected'
    FOREIGN KEY(car_id) REFERENCES Cars(car_id),
    FOREIGN KEY(customer_id) REFERENCES Users(user_id)
);

-- Insert initial car data
INSERT INTO Cars (make, model, year, mileage, available_now, min_rent_period, max_rent_period) VALUES
('Toyota', 'Corolla', 2020, 15000, 1, 1, 30),
('Honda', 'Civic', 2019, 20000, 1, 1, 30),
('Ford', 'Focus', 2018, 22000, 1, 3, 45),
('Chevrolet', 'Malibu', 2021, 5000, 1, 1, 30),
('Tesla', 'Model 3', 2022, 10000, 1, 1, 30);