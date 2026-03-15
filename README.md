# Maju Jaya Data Pipeline

This project demonstrates a simple ETL pipeline using Python, Docker, and MySQL.

## Architecture
CSV → Python ETL → MySQL Database

## Tech Stack
- Python
- Pandas
- SQLAlchemy
- Docker & Docker Compose
- MySQL

## Project Structure
etl/
    Dockerfile
    ingest_customer_addresses.py
    requirements.txt
    data/customer_addresses.csv

mysql/
    init.sql

docker-compose.yml
README.md

## How to Run
1. Clone the repository:
   git clone https://github.com/nataniaadela00/maju-jaya-data-pipeline.git
2. Run the pipeline:
   docker compose up --build
3. The ETL process will ingest CSV data into MySQL automatically.

## Result
The data from `customer_addresses.csv` will be loaded into the MySQL table `customer_addresses`.
