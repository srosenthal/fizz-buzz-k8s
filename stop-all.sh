#!/usr/bin/env bash


echo 'Stopping Docker containers...'

echo '    (fizzer)...'
docker stop fizzer
echo '    (buzzer)...'
docker stop buzzer


echo '... all done! :-D'