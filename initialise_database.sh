#!/usr/bin/env bash

DATABASE_NAME=`cat APPLICATION_NAME`

echo "Dropping database: $DATABASE_NAME..."
dropdb $DATABASE_NAME
echo "Creating database: $DATABASE_NAME..."
createdb $DATABASE_NAME

echo "Loading latest schema into $DATABASE_NAME"
cat architecture/database/latest.sql | psql -d $DATABASE_NAME
echo "Loading default data into $DATABASE_NAME"
cat architecture/database/defaults.sql | psql -d $DATABASE_NAME
echo "DONE!"
