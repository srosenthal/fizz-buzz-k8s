#!/usr/bin/env bash


echo 'Building Docker images...'

echo '    (fizzer)...'
docker build fizzer -t fizzer
echo '    (buzzer)...'
docker build buzzer -t buzzer


echo 'Running Docker containers...'

echo '    (fizzer)...'
docker run --rm -it -d --name fizzer -p 7000:7000 fizzer
echo '    (buzzer)...'
docker run --rm -it -d --name buzzer -p 9000:9000 buzzer


echo 'Waiting a bit...'
sleep 10


echo 'Starting main loop...'
python3 looper/fizzbuzz.py


echo '... all done! :-D'