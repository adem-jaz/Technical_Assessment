# API scraping service for public facebook pages

## Context

The goal of this project is to create a service that scraps data from a facebook public page.
In order to do this, we follow these steps:

- **1st: create a facebook scraper:** a python program that takes the page name and return the data from that page (use of *facebook_scraper* and *facebook-page-scraper*).
- **2nd: save data:** save the returned data in a database (use of *SQLAlchemy*).
- **3rd: API:** Create an API using *fastapi*
- **4th: Dockerization:** dockerize the service and the database with *Docker*.


## How does it work:
To execute this project, follow these steps :
- Clone repository
- run docker-compose up --build (make sure you are in the directory containing the docker-compose.yml file)
- Navigate to 127.0.0.1/scrap/{facebook_page_name} to try the API (exp: 127.0.0.1/RealMadrid)

## Example: Result with metaai
<img width="947" alt="Capture d'écran 2024-01-22 230240" src="https://github.com/adem-jaz/Technical_Assessment/assets/156452749/e25d4cdf-56cc-41ff-807a-a6439d706514">
