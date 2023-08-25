#!/bin/bash

# Build the project
echo "Building the project..."
python3.9 -m pip install -r requirements.txt

export POSTGRES_HOST=containers-us-west-169.railway.app
export POSTGRES_PORT=6048
export POSTGRES_DB=railway
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=JOTH5KG5x3F8WnpjbZRl
export DATABASE_URL=postgresql://postgres:JOTH5KG5x3F8WnpjbZRl@containers-us-west-169.railway.app:6048/railway

echo "Make Migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear