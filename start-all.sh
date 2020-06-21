#!/usr/bin/env bash


echo 'Building Docker images...'

echo '    (fizzer)...'
docker build fizzer -t fizzer
echo '    (buzzer)...'
docker build buzzer -t buzzer
echo '    (looper)...'
docker build looper -t looper


echo 'Running Docker containers...'

echo '    (network)...'
docker network create fizzbuzz_net
echo '    (fizzer)...'
docker run --rm -it -d --name fizzer --net fizzbuzz_net -p 7080:7080 fizzer
echo '    (buzzer)...'
docker run --rm -it -d --name buzzer --net fizzbuzz_net -p 9080:9080 buzzer
echo '    (looper)...'
docker run --rm -it -d --name looper --net fizzbuzz_net -p 8080:8080 looper


echo 'Waiting a bit so the HTTP services can start...'
sleep 10


echo 'Starting main loop...'
curl http://localhost:8080


echo '... all done! :-D'