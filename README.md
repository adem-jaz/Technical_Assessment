# Technical_Assessment
An API scraping service for a facebook page

The goal of this project is to create a service that scraps data from a facebook public page.
In order to do this, we follow these steps:

- 1st: create a facebook scraper: a python program that takes the page name and return the data from that page.
- 2nd: save the returned data in a database
- 3rd: Create an API using Fastapi
- 4th: dockerize the service and the database with Docker


- How does it work:
    - Clone repository
    - run docker-compose up --build (make sure you are in the directory containing the docker-compose.yml file)
    - Navigate to 127.0.0.1/scrap/{facebook_page_name} to try the API (exp: 127.0.0.1/RealMadrid)

- Example : metaai