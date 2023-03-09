@echo off

setlocal EnableDelayedExpansion

for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /i "IPv4 Address"') do (
  set ip=%%a
)

echo Stop all of the running containers
docker-compose down

echo Remove stopped containers
docker container prune -f

echo Create and activate the new venv
virtualenv ENV
ENV\Scripts\activate.bat
pip install -r flask-server\requirements.txt

echo Start the docker containers
set FLASK_APP=flask-server/server.py
docker-compose build --no-cache
docker-compose up -d

echo Waiting for Flask application loads
:loop
powershell -command "& { $response = Invoke-WebRequest -UseBasicParsing -Uri http://%ip%:5000 -Method Head; if ($response.StatusCode -eq 200) { exit 0 } else { Start-Sleep -Seconds 1; goto loop } }"

echo Start the React application
echo Open in browser...
start http://localhost:3000
