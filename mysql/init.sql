CREATE DATABASE IF NOT EXISTS maju_jaya;
USE maju_jaya;

CREATE TABLE customers_raw (
    id INT,
    name VARCHAR(100),
    dob VARCHAR(20),
    created_at DATETIME
);

CREATE TABLE sales_raw (
    vin VARCHAR(20),
    customer_id INT,
    model VARCHAR(50),
    invoice_date DATE,
    price VARCHAR(50),
    created_at DATETIME
);

CREATE TABLE after_sales_raw (
    service_ticket VARCHAR(50),
    vin VARCHAR(20),
    customer_id INT,
    model VARCHAR(50),
    service_date DATE,
    service_type VARCHAR(10),
    created_at DATETIME
);

CREATE TABLE customer_addresses (
    id INT,
    customer_id INT,
    address VARCHAR(255),
    city VARCHAR(100),
    province VARCHAR(100),
    created_at DATETIME
);