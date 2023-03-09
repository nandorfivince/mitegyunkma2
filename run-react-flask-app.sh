#!/bin/bash

IP=$(hostname -I | awk '{print $1}')
export MY_IP=$IP
echo "IP address of the host machine: $IP"
echo "Host IP address environment variable: $MY_IP"

echo "Stop all of the running containers"
docker-compose down

echo "Remove stopped containers"
docker container prune -f

echo "Remove the old venv"
rm -rf venv

echo "Create and activate the new venv"
python3 -m venv venv
source venv/bin/activate
pip install -r flask-server/requirements.txt

echo "Start the docker containers"
docker-compose build --no-cache
docker-compose up -d

echo "Waiting for Flask application loads"
while ! curl -s http://$MY_IP:5000 > /dev/null; do
    sleep 1
done

echo "Start the React application"
echo "Open in browser..."
open http://localhost:3000
