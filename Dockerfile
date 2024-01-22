FROM python:3.9-slim


# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    firefox-esr \
    --no-install-recommends



WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

# Define environment variable
ENV DATABASE_URL sqlite:///./app/database/test.db

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]