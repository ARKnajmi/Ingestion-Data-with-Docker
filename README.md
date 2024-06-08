# 💉 Data Ingestion with Docker
## 🔎 Overview
This project focuses on building a data ingestion pipeline using Docker, Python, Pandas, SQLAlchemy, PostgreSQL. The goal is to efficiently download data from a URL, process it, and load it into a PostgreSQL database.

This is the source dataset that I used in this project: [NYC Taxi](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
## 🧩 Features
* Downloads data from a provided URL (supports both CSV and Parquet formats)
* Cleans and preprocesses the data using Pandas
* Utilizes SQLAlchemy for database interaction
* Supports batch processing for large datasets
* Dockerized for easy deployment and reproducibility

## 🎲 Project Structure
* Dockerfile: Defines the Docker image for the project
* ingest_data.py: Main Python script for data ingestion
* docker-compose.yml: Compose file for setting up PostgreSQL and pgAdmin

## ⬇️ Installation and Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/ARKnajmi/Ingestion-Data-with-Docker.git
   cd Ingestion-Data-with-Docker
   ```

2. Build the Docker image:
   ```bash
   docker build -t data-ingestion .
   ```
   
3. Start the Docker services using Docker Compose:
   ```bash
   docker-compose up -d
   ```   
4. Run the Data Ingestion:
   ```bash
   URL="(Put Your download URL csv or parquet Here)"
   docker run -it \
   --network=ingestion-data-with-docker_default \
   data-ingestion \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --tb=(name of the table) \
    --url=${URL}
   ```
   
5. Access PostgreSQL database:
   * Host: pgdatabase
   * Port: 5432
   * Username: your_username
   * Password: your_password
   * Database: your_database
     
## 👀 Preview
### **pgAdmin**
After starting the Docker services using `docker-compose up -d`, you can access pgAdmin by opening your web browser and navigating to [http://localhost:8080](http://localhost:8080). Use the following credentials to log in:
- **Username:** admin@admin.com
- **Password:** root

![pgAdmin Preview](https://github.com/ARKnajmi/Ingestion-Data-with-Docker/assets/149140186/2196ea4a-c8dd-4c35-aa59-cd89f3bae731)

First of all, you need to register your server database and establish a connection. make sure the host, username, and password are the same as the ones in docker compose.

### **Preview of Data Ingestion**
Running the data ingestion script will download the specified data file, clean and preprocess it, and then insert it into the PostgreSQL database. Here's a sample output of the ingestion process:

![Data Ingestion Preview](https://github.com/ARKnajmi/Ingestion-Data-with-Docker/assets/149140186/abba28d1-5f6e-449f-9816-10752f5daa15)

![Data Ingestion Preview](https://github.com/ARKnajmi/Ingestion-Data-with-Docker/assets/149140186/3435e23e-9046-457e-8452-ee1fcc3b7e3e)

**The data is now stored in your database:**

![Data Ingestion Preview](https://github.com/ARKnajmi/Ingestion-Data-with-Docker/assets/149140186/f58760d0-c9f5-4380-a244-6189e50655f6)



   
