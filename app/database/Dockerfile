# Use a smaller base image
FROM docker.io/library/alpine:latest

# Set the working directory
WORKDIR /code

# Install SQLite
RUN apk --no-cache add sqlite

# Copy the database file
COPY ./test.db /code/test.db

# Set the default command to run when the container starts
CMD ["sh"]