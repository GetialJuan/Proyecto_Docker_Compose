FROM postgres

COPY ./database/schema.sql /docker-entrypoint-initdb.d/schema.sql