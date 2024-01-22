FROM docker.io/library/alpine:latest

WORKDIR /code

RUN apk --no-cache add sqlite

COPY ./test.db /code/test.db

CMD ["sh"]