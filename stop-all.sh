#!/usr/bin/env bash


echo 'Stopping Docker containers...'

echo '    (fizzer)...'
docker stop fizzer
echo '    (buzzer)...'
docker stop buzzer
echo '    (looper)...'
docker stop looper
echo '    (network)...'
docker network rm fizzbuzz_net


echo '... all done! :-D'